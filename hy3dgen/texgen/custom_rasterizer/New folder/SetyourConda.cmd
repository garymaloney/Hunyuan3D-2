@echo off
echo [1/4] Setting Environment Variables...
:: Set your Conda .venv as the CUDA_HOME
set "CUDA_HOME=C:\Users\coryc\Documents\My_GPU_Project\.venv"
set "PATH=%CUDA_HOME%\bin;%CUDA_HOME%\Library\bin;%PATH%"

:: Force Python to use the SDK instead of hunting for VS 2019
set "DISTUTILS_USE_SDK=1"
set "FORCE_CUDA=1"

echo [2/4] Activating Python Environment...
call C:\Users\coryc\anaconda3\Scripts\activate.bat C:\Users\coryc\Documents\My_GPU_Project\.venv

echo [3/4] Activating VS 2022 Compiler...
:: This bypasses the "path not found" errors for VS 2019 seen in your logs
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"

echo [4/4] Starting Build...
cd /d "C:\Users\coryc\Documents\GitHub\Hunyuan3D-2\hy3dgen\texgen\custom_rasterizer"
python setup.py install

echo.
echo If it finished, check for "Success". If it failed, read the error above.
:: This keeps the window open even after the script finishes
cmd /k