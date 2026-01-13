@echo off
:: Your existing activation and setup commands here...
call C:\Users\coryc\anaconda3\Scripts\activate.bat C:\Users\coryc\Documents\My_GPU_Project\.venv
cd C:\Users\coryc\Documents\GitHub\Hunyuan3D-2\hy3dgen\texgen\custom_rasterizer

:: This is the magic line that keeps it open and lets you keep typing
cmd /k