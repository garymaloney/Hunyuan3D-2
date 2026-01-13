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
module = load(name='custom_rasterizer_kernel', sources=sources, verbose=True)
print('Built module:', module)
