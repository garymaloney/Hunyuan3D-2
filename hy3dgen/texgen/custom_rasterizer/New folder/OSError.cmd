
@echo off
echo Step 1: Setting up CUDA Environment...
:: Manually set the CUDA path to stop the "OSError: CUDA_HOME"
set "CUDA_HOME=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v13.1"
set "CUDNN_HOME=%CUDA_HOME%"

echo Step 2: Activating Python Environment...
:: Activate your specific project environment
call C:\Users\coryc\anaconda3\Scripts\activate.bat C:\Users\coryc\Documents\My_GPU_Project\.venv

echo Step 3: Activating Visual Studio Compiler...
:: This bypasses the broken 2019 search and uses your VS 2022 tools
:: NOTE: If this path fails, check if you have 'Community' or 'BuildTools'
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"

echo Step 4: Forcing Build Flags...
:: Tells Python to use the current window's VS settings and ignore 2019 hunting
set "DISTUTILS_USE_SDK=1"
set "MSSdk=1"

echo Step 5: Starting Compilation...
:: Navigates to the correct folder and starts the build
cd /d "C:\Users\coryc\Documents\GitHub\Hunyuan3D-2\hy3dgen\texgen\custom_rasterizer"
python setup.py install

echo Done!
cmd /k