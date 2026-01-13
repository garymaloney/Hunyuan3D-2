import subprocess
import sys
pyd = r"C:\Users\coryc\AppData\Local\torch_extensions\torch_extensions\Cache\py311_cu124\custom_rasterizer_kernel\custom_rasterizer_kernel.pyd"
dumpbin = r"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.44.35207\bin\Hostx64\x64\dumpbin.exe"
try:
    proc = subprocess.run([dumpbin, '/dependents', pyd], capture_output=True, text=True)
    print('returncode=', proc.returncode)
    print('STDOUT:\n', proc.stdout)
    print('STDERR:\n', proc.stderr)
except Exception as e:
    print('ERROR', e)
    sys.exit(2)
