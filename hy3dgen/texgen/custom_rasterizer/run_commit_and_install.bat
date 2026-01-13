@echo off
REM Commit changes if git is available, then perform a safe editable install

where git >nul 2>&1
if %ERRORLEVEL%==0 (
  echo Git found — committing changes
  git add -A
  git commit -m "Fix: Add DLL loader helpers and build/test scripts; ensure custom_rasterizer imports in dev env" || (
    echo Git commit failed or nothing to commit, continuing...
  )
) else (
  echo Git not found in PATH — skipping commit
)

echo Starting editable install inside Developer Command Prompt (shortened PATH)
set "OLD_PATH=%PATH%"
set "PATH=C:\Windows\system32;C:\Windows"
set DISTUTILS_USE_SDK=1
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"
"C:\Users\coryc\miniconda3\envs\py311_rasterizer\python.exe" build_ext.py
set "PATH=%OLD_PATH%"

echo Done. Check output above for errors.
exit /b %ERRORLEVEL%
@echo off
REM Commit changes if git is available, then perform a safe editable install

where git >nul 2>&1
if %ERRORLEVEL%==0 (
  echo Git found — committing changes
  git add -A
  git commit -m "Fix: Add DLL loader helpers and build/test scripts; ensure custom_rasterizer imports in dev env" || (
    echo Git commit failed or nothing to commit, continuing...
  )
) else (
  echo Git not found in PATH — skipping commit
)

echo Starting editable install inside Developer Command Prompt (shortened PATH)
set "OLD_PATH=%PATH%"
set "PATH=C:\Windows\system32;C:\Windows"
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"
"C:\Users\coryc\miniconda3\envs\py311_rasterizer\python.exe" -m pip install -e .
set "PATH=%OLD_PATH%"

echo Done. Check output above for errors.
exit /b %ERRORLEVEL%
