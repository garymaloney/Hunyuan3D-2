@echo off
REM Shorten PATH, set DISTUTILS_USE_SDK, run vcvars64, then pip install editable without build isolation
set "OLD_PATH=%PATH%"
set "PATH=C:\Windows\system32;C:\Windows"
set DISTUTILS_USE_SDK=1
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"
"C:\Users\coryc\miniconda3\envs\py311_rasterizer\python.exe" -m pip install -e . --no-build-isolation
set "PATH=%OLD_PATH%"
exit /b %ERRORLEVEL%
