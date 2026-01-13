import torch
print(torch.cuda.is_available()) # For NVIDIA
# or for Apple Silicon:
# print(torch.backends.mps.is_available())
