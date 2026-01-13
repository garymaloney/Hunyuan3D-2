@echo off
set "OLD_PATH=%PATH%"
set "PATH=C:\Windows\system32;C:\Windows"
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"
"C:\Users\coryc\miniconda3\envs\py311_rasterizer\python.exe" build_ext.py
if errorlevel 1 exit /b %ERRORLEVEL%
"C:\Users\coryc\miniconda3\envs\py311_rasterizer\python.exe" test_import.py
set "PATH=%OLD_PATH%"
exit /b %ERRORLEVEL%
