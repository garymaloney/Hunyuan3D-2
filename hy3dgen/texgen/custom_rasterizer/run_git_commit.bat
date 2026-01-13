@echo off
"C:\Program Files\Git\bin\git.exe" add -A
"C:\Program Files\Git\bin\git.exe" commit -m "Fix: Add DLL loader helpers and build/test scripts; ensure custom_rasterizer imports in dev env" || (
  echo no-changes-committed
)
exit /b %ERRORLEVEL%
