import os
import sys
# set CUDA_HOME for this process
cuda_candidate = r'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v13.1'
if os.path.isdir(cuda_candidate):
    os.environ['CUDA_HOME'] = cuda_candidate
    os.environ['CUDA_PATH'] = cuda_candidate
    os.environ['PATH'] = os.path.join(cuda_candidate, 'bin') + os.pathsep + os.environ.get('PATH', '')
    print('Using CUDA_HOME =', cuda_candidate)
else:
    print('CUDA candidate not found:', cuda_candidate)

sources = [
    'lib/custom_rasterizer_kernel/rasterizer.cpp',
    'lib/custom_rasterizer_kernel/grid_neighbor.cpp',
    'lib/custom_rasterizer_kernel/rasterizer_gpu.cu',
]
print('Starting build via torch.utils.cpp_extension.load...')
# If torch.utils.cpp_extension was previously imported without CUDA env set,
# remove it from sys.modules so it reloads and picks up our CUDA_HOME.
for key in list(sys.modules.keys()):
    if key.startswith('torch.utils.cpp_extension') or key == 'torch.utils.cpp_extension':
        del sys.modules[key]
# Do NOT remove the top-level 'torch' package — removing it can cause
# runtime errors (double-registration). Only remove the cpp_extension
# submodule so it will be re-imported with the updated environment.
import importlib
cpp_mod = importlib.import_module('torch.utils.cpp_extension')
# Remove stray nsight-compute entries from PATH that point to non-existent helpers
# (some conda packages add nsight paths that reference python.bat which may not exist).
path_parts = os.environ.get('PATH', '').split(os.pathsep)
filtered = []
for p in path_parts:
    lp = p.lower()
    if 'nsight-compute' in lp:
        if os.path.isdir(p):
            # keep only if directory exists and contains a usable exe
            if any(os.path.isfile(os.path.join(p, f)) for f in ('nsight-compute.exe', 'nv-nsight-cu-cli.exe', 'python.bat')):
                filtered.append(p)
            else:
                print('Removing broken nsight-compute PATH entry:', p)
        else:
            print('Removing missing nsight-compute PATH entry:', p)
    else:
        filtered.append(p)
os.environ['PATH'] = os.pathsep.join(filtered)
# Ensure module sees our CUDA_HOME
if hasattr(cpp_mod, 'CUDA_HOME'):
    cpp_mod.CUDA_HOME = os.environ.get('CUDA_HOME')
if hasattr(cpp_mod, 'CUDA_PATH'):
    cpp_mod.CUDA_PATH = os.environ.get('CUDA_HOME')
# Ensure TORCH_CUDA_ARCH_LIST is set so nvcc architecture flags are generated.
if 'TORCH_CUDA_ARCH_LIST' not in os.environ:
    # Common architectures; adjust if you know your GPU (e.g., '8.6' for RTX 40xx)
    os.environ['TORCH_CUDA_ARCH_LIST'] = '7.5;8.0;8.6'
load = getattr(cpp_mod, 'load')
try:
    module = load(name='custom_rasterizer_kernel', sources=sources, verbose=True)
    print('Built module:', module)
except Exception as e:
    msg = str(e).lower()
    if 'nsight' in msg or 'python.bat' in msg or 'could not find files' in msg:
        print('Warning: nsight-compute helper error detected, falling back to CPU-only build.')
        cpu_sources = [s for s in sources if not s.endswith('.cu')]
        try:
            module = load(name='custom_rasterizer_kernel', sources=cpu_sources, verbose=True)
            print('Built CPU-only module:', module)
        except Exception as e2:
            print('CPU-only fallback also failed:', e2)
            raise
    else:
        raise
