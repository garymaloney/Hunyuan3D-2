import sys, traceback, importlib.util
print('executable:', sys.executable)
print('version:', sys.version)
print('setuptools:', __import__('setuptools').__version__)
print('find_spec(pygltflib):', importlib.util.find_spec('pygltflib'))
try:
    import custom_rasterizer as cr
    print('custom_rasterizer loaded:', getattr(cr, '__file__', repr(cr)))
except Exception:
    traceback.print_exc()
    sys.exit(1)
