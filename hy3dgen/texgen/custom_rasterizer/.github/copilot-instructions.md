# Copilot / Agent instructions — custom_rasterizer

Short, actionable guidance to make code changes and builds productive in this repository.

- **Big picture:** This package exposes a Python API (`custom_rasterizer`) that wraps a native PyTorch extension named `custom_rasterizer_kernel`. Native sources live under `lib/custom_rasterizer_kernel/` and include both CPU C++ (`*.cpp`) and optional CUDA (`*.cu`) implementations. Python entry points that call the extension include [custom_rasterizer/render.py](custom_rasterizer/render.py) and [custom_rasterizer/__init__.py](custom_rasterizer/__init__.py).

- **Build vs runtime paths:** Building uses either `torch.utils.cpp_extension` (CUDAExtension) or a fallback CPU `Extension`. Key build helpers:
  - [setup.py](setup.py): chooses CUDA vs CPU builds, tries to auto-detect `CUDA_HOME`, and returns `ext_modules`/`cmdclass` for `setup()`.
  - [build_ext.py](build_ext.py): loads the extension via `torch.utils.cpp_extension.load()` and explicitly sets `TORCH_CUDA_ARCH_LIST` and `CUDA_HOME` for reliable nvcc use on Windows.
  - Windows helper scripts: [run_build_with_vcvars.bat](run_build_with_vcvars.bat) and [run_build_and_test.bat](run_build_and_test.bat) call `vcvars64.bat`, run `build_ext.py`, then `test_import.py`.

- **Recommended dev workflow (Windows, matching repo):**
  1. Activate a conda env with torch (preferably CUDA-enabled). Update paths in the .bat files if needed.
 2. Run `run_build_with_vcvars.bat` (or `run_build_and_test.bat`) to prepare VC++ environment and build. These scripts use an explicit Python path — update to your interpreter or run them from an activated env.
 3. After build, run `test_import.py` (already called from the `.bat`) to verify the extension imports.

- **Important behaviors and gotchas:**
  - `setup.py` will try to auto-set `CUDA_HOME` from common Windows install locations. If nvcc is not found, the build falls back to a CPU-only extension (it strips `.cu` from sources).
  - `build_ext.py` removes `torch.utils.cpp_extension` from `sys.modules` before re-importing so the module picks up updated env-vars; avoid importing the extension prior to running the build script.
  - `custom_rasterizer/__init__.py` uses `os.add_dll_directory()` to add conda and torch DLL dirs on Windows. Ensure those DLL directories are present or imports will fail.

- **Python API patterns to mirror in changes:**
  - `render.rasterize(pos, tri, resolution, clamp_depth, use_depth_prior)` expects `pos` and `tri` on the same device and calls `custom_rasterizer_kernel.rasterize_image(...)`.
  - `io_glb.LoadGlb(path)` returns `primitives` (list of dicts) and `images` mapping. Expect keys like `V` (vertices), `F` (faces), `VC` (vertex colors), `UV`, `TEX`, `MC` (material color).

- **When editing native code:**
  - Modify sources under `lib/custom_rasterizer_kernel/` (e.g., `rasterizer.cpp`, `rasterizer_gpu.cu`). Keep Python-visible function names (the extension exports `rasterize_image`, `build_hierarchy`, etc.).
  - Keep GPU/CPU parity in mind: `setup.py` may exclude `.cu` for CPU-only builds — ensure CPU fallbacks exist if you change GPU logic.

- **Where to look for examples/tests:**
  - Small runtime check: [test_import.py](test_import.py) — import validation.
  - Build helper and environment tweaks: [build_ext.py](build_ext.py) and the two .bat scripts.

- **Files to reference while coding:**
  - [setup.py](setup.py)
  - [build_ext.py](build_ext.py)
  - [run_build_and_test.bat](run_build_and_test.bat)
  - [run_build_with_vcvars.bat](run_build_with_vcvars.bat)
  - [custom_rasterizer/render.py](custom_rasterizer/render.py)
  - [custom_rasterizer/io_glb.py](custom_rasterizer/io_glb.py)
  - [lib/custom_rasterizer_kernel/](lib/custom_rasterizer_kernel/) (native sources)

- **Do not assume:**
  - That `nvcc` is on PATH — the repo relies on `CUDA_HOME` detection and `vcvars` on Windows.
  - That tests exist beyond `test_import.py` — add focused tests when changing APIs or native behavior.

If anything here is unclear or you want a different level of detail (examples of editing the CUDA kernel, packaging notes, or CI-friendly build instructions), tell me which area to expand. 
