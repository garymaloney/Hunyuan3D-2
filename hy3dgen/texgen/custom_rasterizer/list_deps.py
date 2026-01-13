import os
paths = [r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v13.1\bin", r"C:\Users\coryc\miniconda3\envs\py311_rasterizer\Lib\site-packages\torch\lib"]
for p in paths:
    print('==', p)
    try:
        for f in sorted(os.listdir(p)):
            print(f)
    except Exception as e:
        print('ERROR', e)
    print()
