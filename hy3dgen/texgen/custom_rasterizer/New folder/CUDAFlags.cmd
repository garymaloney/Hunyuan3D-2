@echo off
echo [1/3] Setting CUDA and Flags...
:: Use your Conda .venv as the CUDA_HOME
set "CUDA_HOME=C:\Users\coryc\Documents\My_GPU_Project\.venv"
set "PATH=%CUDA_HOME%\bin;%CUDA_HOME%\Library\bin;%PATH%"
set "DISTUTILS_USE_SDK=1"
set "FORCE_CUDA=1"

echo [2/3] Activating VS 2022 Compiler...
:: This replaces the broken 2019 calls from your logs
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat" || (echo VS 2022 NOT FOUND && pause && exit)

echo [3/3] Running Build...
cd /d "C:\Users\coryc\Documents\GitHub\Hunyuan3D-2\hy3dgen\texgen\custom_rasterizer" || (echo FOLDER NOT FOUND && pause && exit)

:: Run the install and force the window to stay open at the end
python setup.py install
if %errorlevel% neq 0 (
    echo.
    echo BUILD FAILED! Check the errors above.
    pause
)
echo.
echo Script finished.
cmd /k