:: 1. Initialize the tools using the WORKING 2022 path
call "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat"

:: 2. Set the flag to use these tools
set DISTUTILS_USE_SDK=1

:: 3. Run your build
python setup.py install
cmd /k