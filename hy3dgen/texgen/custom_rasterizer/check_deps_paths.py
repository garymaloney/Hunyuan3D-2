import shutil, os
deps = [
 'c10.dll','c10_cuda.dll','torch_cpu.dll','torch_cuda.dll','torch_python.dll',
 'MSVCP140.dll','python311.dll','KERNEL32.dll','VCRUNTIME140.dll','VCRUNTIME140_1.dll']
search_paths = [r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\Lib\site-packages\torch\lib",
                r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\bin",
                r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\Library\bin",
                r"C:\Windows\System32",
                r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v13.1\bin"]
for d in deps:
    print('==', d)
    found = False
    for p in search_paths:
        candidate = os.path.join(p, d)
        if os.path.exists(candidate):
            print('  found in', candidate)
            found = True
    if not found:
        p = shutil.which(d)
        print('  which() ->', p)
    print()
