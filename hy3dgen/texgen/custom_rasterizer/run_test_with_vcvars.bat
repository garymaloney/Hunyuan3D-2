@echo off
set "OLD_PATH=%PATH%"
set "PATH=C:\Windows\system32;C:\Windows;C:\Users\coryc\miniconda3\envs\py311_rasterizer\bin;C:\Users\coryc\miniconda3\envs\py311_rasterizer\Library\bin;C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v13.1\bin"
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"
"C:\Users\coryc\miniconda3\envs\py311_rasterizer\python.exe" test_import.py
set "PATH=%OLD_PATH%"
exit /b %ERRORLEVEL%
