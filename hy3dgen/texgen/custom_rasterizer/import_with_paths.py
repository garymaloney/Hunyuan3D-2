import os,sys
env_bin = r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\bin"
lib_bin = r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\Library\bin"
torch_lib = r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\Lib\site-packages\torch\lib"
cuda_bin = r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v13.1\bin\x64"
paths = [env_bin, lib_bin, torch_lib, cuda_bin]
old = os.environ.get('PATH','')
for p in paths:
    if p and p not in old:
        old = p + os.pathsep + old
os.environ['PATH'] = old
print('PATH set to include:', paths)
try:
    import importlib
    m = importlib.import_module('custom_rasterizer')
    print('Imported', m)
    print('module file:', getattr(m,'__file__',None))
except Exception as e:
    import traceback
    traceback.print_exc()
    sys.exit(1)
