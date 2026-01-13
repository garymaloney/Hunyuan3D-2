import importlib
m = importlib.import_module('custom_rasterizer')
print('Imported', m)
print('custom_rasterizer.__file__ =', getattr(m, '__file__', None))
