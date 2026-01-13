@echo off
echo [1/4] Setting Conda CUDA paths...
:: Use the path to your active Conda environment
set "CONDA_ENV_PATH=C:\Users\coryc\Documents\My_GPU_Project\.venv"
set "CUDA_HOME=%CONDA_ENV_PATH%"
set "PATH=%CONDA_ENV_PATH%\bin;%CONDA_ENV_PATH%\Library\bin;%PATH%"

echo [2/4] Activating Python and Compiler...
:: Activate your environment
call C:\Users\coryc\anaconda3\Scripts\activate.bat %CONDA_ENV_PATH%

:: Manually call the VS 2022 tools to bypass the broken 2019 search
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"

echo [3/4] Forcing Build Environment...
:: Stop the script from looking for VS 2019 folders
set "DISTUTILS_USE_SDK=1"
set "FORCE_CUDA=1"

echo [4/4] Starting Build...
cd /d "C:\Users\coryc\Documents\GitHub\Hunyuan3D-2\hy3dgen\texgen\custom_rasterizer"
python setup.py install

echo Done! If you see 'Success', the rasterizer is ready.
cmd /k