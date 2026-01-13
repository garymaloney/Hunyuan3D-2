try:
    from setuptools import setup, find_packages
except Exception:
    # Minimal fallbacks if setuptools is not available (e.g., static analysis)
    try:
        import importlib
        import importlib.util
        dist_spec = importlib.util.find_spec("distutils.core")
        if dist_spec is not None:
            distutils_core = importlib.import_module("distutils.core")
            setup = getattr(distutils_core, "setup")
        else:
            raise ImportError("distutils.core not found")
    except Exception:
        def setup(*args, **kwargs):
            raise RuntimeError("setuptools or distutils is required to build this package")
    def find_packages():
        return []

# Auto-detect CUDA_HOME if not set (helps BuildExtension find nvcc on Windows)
import os
def _detect_and_set_cuda_home():
    if 'CUDA_HOME' in os.environ and os.path.isdir(os.environ['CUDA_HOME']):
        return
    cuda_root = r'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA'
    try:
        if os.path.isdir(cuda_root):
            versions = [d for d in os.listdir(cuda_root) if os.path.isdir(os.path.join(cuda_root, d))]
            if versions:
                versions.sort(reverse=True)
                detected = os.path.join(cuda_root, versions[0])
                # ensure nvcc exists in the detected path
                nvcc_path = os.path.join(detected, 'bin', 'nvcc.exe')
                if os.path.isfile(nvcc_path):
                    os.environ['CUDA_HOME'] = detected
                    os.environ['CUDA_PATH'] = detected
                    # prepend to PATH for this process
                    os.environ['PATH'] = detected + os.pathsep + os.path.join(detected, 'bin') + os.pathsep + os.environ.get('PATH', '')
                    print('Auto-set CUDA_HOME to', detected)
                else:
                    # still set CUDA_HOME to detected even if nvcc not found; BuildExtension may search other places
                    os.environ['CUDA_HOME'] = detected
                    os.environ['CUDA_PATH'] = detected
                    os.environ['PATH'] = os.path.join(detected, 'bin') + os.pathsep + os.environ.get('PATH', '')
                    print('Auto-set CUDA_HOME (nvcc missing) to', detected)
    except Exception:
        pass

_detect_and_set_cuda_home()

def get_extensions_and_cmdclass():
    import importlib
    import importlib.util
    # ensure CUDA_HOME is set for torch BuildExtension checks
    if 'CUDA_HOME' not in os.environ:
        # try common install locations
        candidates = [
            r'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v13.1',
            r'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v13.0',
            r'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA',
        ]
        for c in candidates:
            if os.path.isdir(c):
                os.environ['CUDA_HOME'] = c
                os.environ['CUDA_PATH'] = c
                os.environ['PATH'] = os.path.join(c, 'bin') + os.pathsep + os.environ.get('PATH', '')
                print('Set CUDA_HOME for build to', c)
                break
    try:
        torch_spec = importlib.util.find_spec("torch.utils.cpp_extension")
        if torch_spec is not None:
            torch_cpp = importlib.import_module("torch.utils.cpp_extension")
            BuildExtension = getattr(torch_cpp, "BuildExtension")
            CUDAExtension = getattr(torch_cpp, "CUDAExtension")
        else:
            raise ImportError("torch.utils.cpp_extension not found")
    except Exception:
        try:
            from setuptools import Extension as CUDAExtension
            from setuptools.command.build_ext import build_ext as BuildExtension
        except Exception:
            from distutils.core import Extension as CUDAExtension
            from distutils.command.build_ext import build_ext as BuildExtension

    sources = [
        'lib/custom_rasterizer_kernel/rasterizer.cpp',
        'lib/custom_rasterizer_kernel/grid_neighbor.cpp',
        'lib/custom_rasterizer_kernel/rasterizer_gpu.cu',
    ]
    # Decide whether to build CUDA extension or fall back to a CPU-only C++ extension.
    use_cuda_ext = False
    try:
        import torch
        # torch.version.cuda may be a string like '13.1' when CUDA-enabled torch is installed
        has_torch_cuda = getattr(torch.version, 'cuda', None) is not None
        has_torch_cuda = has_torch_cuda and hasattr(torch, 'cuda') and torch.cuda.is_available()
        if has_torch_cuda and os.environ.get('CUDA_HOME'):
            use_cuda_ext = True
    except Exception:
        use_cuda_ext = False

    if use_cuda_ext:
        ext = CUDAExtension('custom_rasterizer_kernel', sources)
    else:
        # Build a CPU-only extension (exclude .cu) so package can be used without CUDA
        try:
            from setuptools import Extension
            cpu_sources = [s for s in sources if not s.endswith('.cu')]
            include_dirs = []
            try:
                # Try to get torch include paths if available
                import torch
                try:
                    from torch.utils.cpp_extension import include_paths
                    include_dirs = include_paths()
                except Exception:
                    pass
            except Exception:
                pass
            ext = Extension('custom_rasterizer_kernel', cpu_sources, include_dirs=include_dirs)
        except Exception:
            # Fallback to original behavior: attempt to build full CUDAExtension
            ext = CUDAExtension('custom_rasterizer_kernel', sources)

    return [ext], {'build_ext': BuildExtension}


# build custom rasterizer
# build with `python setup.py install`
# nvcc is needed

ext_modules, cmdclass = get_extensions_and_cmdclass()

setup(
    packages=find_packages(),
    version='0.1',
    name='custom_rasterizer',
    include_package_data=True,
    package_dir={'': '.'},
    ext_modules=ext_modules,
    cmdclass=cmdclass,
)
