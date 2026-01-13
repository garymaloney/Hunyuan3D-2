import torch, os, sys
print('PY_EXE', sys.executable)
print('TORCH', torch.__version__, getattr(torch.version,'cuda',None), torch.cuda.is_available())
tp = os.path.dirname(torch.__file__)
print('TORCH_PATH', tp)
print('HEADER_EXISTS', os.path.exists(os.path.join(tp, 'include', 'torch', 'extension.h')))
try:
    from torch.utils.cpp_extension import include_paths
    print('CPP_INCLUDE_PATHS', include_paths())
except Exception as e:
    print('CPP_EXT_ERROR', e)
