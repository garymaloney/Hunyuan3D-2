# Install CUDA Toolkit (specify version if needed, e.g., 13.1.0)
conda install -c nvidia nvidia::cuda-toolkit=13.1.0 # or conda-forge::cudatoolkit=13.1.0

# Install cuDNN (often required for DL frameworks)
conda install -c conda-forge cudnn # Or a specific version like cudnn=8.9.0
