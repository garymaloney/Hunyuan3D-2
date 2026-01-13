import os, ctypes
paths = [r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\bin",
         r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\Library\bin",
         r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\Lib\site-packages\torch\lib",
         r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v13.1\bin\x64"]
old = os.environ.get('PATH','')
for p in paths:
    old = p + os.pathsep + old
os.environ['PATH'] = old
print('PATH set')
# candidate files to try loading (full paths if possible)
cands = [
 r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\Lib\site-packages\torch\lib\c10.dll",
 r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\Lib\site-packages\torch\lib\c10_cuda.dll",
 r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\Lib\site-packages\torch\lib\torch_cpu.dll",
 r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\Lib\site-packages\torch\lib\torch_cuda.dll",
 r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\Lib\site-packages\torch\lib\torch_python.dll",
 r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\Library\bin\MSVCP140.dll",
 r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\python311.dll",
 r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\Library\bin\VCRUNTIME140.dll",
 r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\Library\bin\VCRUNTIME140_1.dll",
 r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\bin\cublas64_12.dll",
 r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\bin\cublasLt64_12.dll",
 r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\bin\cusparse64_12.dll",
 r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\bin\cufft64_11.dll",
 r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\bin\cusolver64_11.dll",
 r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\bin\cudart64_12.dll",
 r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v13.1\bin\x64\cusparse64_12.dll"
]
for f in cands:
    try:
        print('Loading', f)
        ctypes.WinDLL(f)
        print('  OK')
    except Exception as e:
        print('  FAIL', e)
