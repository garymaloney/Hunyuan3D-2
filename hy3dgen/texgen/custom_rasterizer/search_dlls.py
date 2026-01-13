import glob
import os
candidates = []
search_paths = [r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v13.1\bin",
                r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\Library\bin",
                r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\Lib\site-packages\torch\lib"]
patterns = ["cudart*.dll", "cudnn*.dll", "cublas*.dll", "cudnn64_*.dll"]
for p in search_paths:
    print('==', p)
    for pat in patterns:
        found = glob.glob(os.path.join(p, pat))
        for f in found:
            print(os.path.basename(f))
    print()
