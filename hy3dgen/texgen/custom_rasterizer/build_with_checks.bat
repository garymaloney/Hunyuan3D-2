@echo off
echo === Shorten PATH for vcvars initialization ===
set PATH=C:\Windows\System32;C:\Windows
:: Add Visual Studio VC auxiliary build directory so vcvars64.bat can be called by name
set "VC_AUX_BUILD_DIR=C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build"
set "PATH=%VC_AUX_BUILD_DIR%;%PATH%"

echo === Call vcvars64 to configure MSVC ===
call vcvars64.bat
if errorlevel 1 (
  echo vcvars64 failed
  exit /b 1
)

echo === Check compiler and nvcc locations ===
where cl || echo cl not found
where nvcc || echo nvcc not found

echo === Activate conda env tools on PATH ===
set PATH=C:\Users\coryc\miniconda3\envs\py311_rasterizer\Scripts;C:\Users\coryc\miniconda3\envs\py311_rasterizer\Library\bin;C:\Windows\System32;C:\Windows

echo === Use system CUDA 12.4 ===
set CUDA_HOME=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4
set CUDA_PATH=%CUDA_HOME%
:: Construct a minimal, safe PATH that excludes nsight entries and long PATH expansions
set "MSVC_HOST_BIN=C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.44.35207\bin\Hostx64\x64"
set "CONDA_ENV_SCRIPTS=C:\Users\coryc\miniconda3\envs\py311_rasterizer\Scripts"
set "CONDA_ENV_LIBBIN=C:\Users\coryc\miniconda3\envs\py311_rasterizer\Library\bin"
set "WIN_KITS_BIN=C:\Program Files (x86)\Windows Kits\10\bin\10.0.26100.0\x64"
set PATH=%MSVC_HOST_BIN%;%WIN_KITS_BIN%;%CONDA_ENV_SCRIPTS%;%CONDA_ENV_LIBBIN%;%CUDA_HOME%\bin;%CUDA_HOME%\lib\x64;C:\Windows\System32;C:\Windows

echo === nvcc version ===
nvcc --version || echo nvcc not runnable

echo === Build native extension in-place ===
:: Run build_ext.py with a filtered PATH (remove nsight-compute entries) using PowerShell
set "CONDA_PY=%CONDA_ENV_SCRIPTS%\python.exe"
set "POWERSHELL_PATH=%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe"
"%POWERSHELL_PATH%" -NoProfile -Command "& { $p=($env:PATH -split ';') | Where-Object { $_ -and ($_ -notmatch 'nsight-compute') }; $env:PATH = ($p -join ';'); exit (& '%CONDA_PY%' 'build_ext.py') }" || (
  echo build_ext.py failed
  exit /b 1
)

echo === Install editable package ===
set DISTUTILS_USE_SDK=1
pip install -e . --no-build-isolation -v || (
  echo pip editable install failed
  exit /b 1
)

echo === Test import ===
python -c "import custom_rasterizer; print('import OK')" || (
  echo import test failed
  exit /b 1
)
echo All steps completed successfully
exit /b 0
