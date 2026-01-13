@echo off
:: Shorten PATH to avoid 'input line too long' when calling vcvars64
:: Use a short PATH that includes the conda env's Scripts and Library bins so pip is available
set PATH=C:\Users\coryc\miniconda3\envs\py311_rasterizer\Scripts;C:\Users\coryc\miniconda3\envs\py311_rasterizer\Library\bin;C:\Windows\System32;C:\Windows
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"
if errorlevel 1 (
    echo Failed to call vcvars64.bat
    exit /b 1
)
:: Ensure conda env tools (pip/python) are on PATH after vcvars
:: Ensure conda env tools (pip/python) are on PATH after vcvars
set PATH=C:\Users\coryc\miniconda3\envs\py311_rasterizer\Scripts;C:\Users\coryc\miniconda3\envs\py311_rasterizer\Library\bin;C:\Windows\System32;C:\Windows
:: Use system CUDA 12.4 installation for nvcc and runtime (user-installed)
set CUDA_HOME=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4
set CUDA_PATH=%CUDA_HOME%
set PATH=%CUDA_HOME%\bin;%CUDA_HOME%\lib\x64;%PATH%
set DISTUTILS_USE_SDK=1
pip install -e . --no-build-isolation -v
exit /b %ERRORLEVEL%
