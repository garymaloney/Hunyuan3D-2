:: 1. Navigate to your project
cd /d "C:\Users\coryc\Documents\GitHub\Hunyuan3D-2\hy3dgen\texgen\custom_rasterizer"

:: 2. Set the CUDA home to your Conda env (as you mentioned)
set "CUDA_HOME=C:\Users\coryc\Documents\My_GPU_Project\.venv"

:: 3. Tell Python to use the tools already active in this window
set "DISTUTILS_USE_SDK=1"

:: 4. Run the installation
python setup.py install