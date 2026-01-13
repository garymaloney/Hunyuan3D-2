@echo off
:: minimize PATH to avoid "input line is too long" errors, vcvars will prepend necessary entries
set "OLD_PATH=%PATH%"
set "PATH=C:\Windows\system32;C:\Windows"
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"
:: restore PATH so python and conda runtime can be found if needed
"C:\Users\coryc\miniconda3\envs\py311_rasterizer\python.exe" build_ext.py
exit /b %ERRORLEVEL%
