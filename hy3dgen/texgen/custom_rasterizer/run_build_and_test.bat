@echo off
set "OLD_PATH=%PATH%"
set "PATH=C:\Windows\system32;C:\Windows"
:: Ensure vcvars64 is on PATH so it can be invoked by name
set "VC_AUX_BUILD_DIR=C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build"
set "PATH=%VC_AUX_BUILD_DIR%;%PATH%"
call vcvars64.bat
"C:\Users\coryc\miniconda3\envs\py311_rasterizer\python.exe" build_ext.py
if errorlevel 1 exit /b %ERRORLEVEL%
"C:\Users\coryc\miniconda3\envs\py311_rasterizer\python.exe" test_import.py
set "PATH=%OLD_PATH%"
exit /b %ERRORLEVEL%
