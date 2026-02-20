# Image Processing with Pillow in Python

A collection of Python scripts exploring basic to intermediate image processing techniques using the **Pillow** (PIL fork) library, along with NumPy and Matplotlib for array manipulation and visualization.

This repository was built step-by-step through interactive learning sessions — starting from opening & displaying images, moving to channel manipulation, quantization, concatenation, reference vs copy behavior, cropping, and more.

## What's Inside

| File / Notebook | Description | Main Concepts Covered |
|-----------------|-------------|-----------------------|
| `rgb-pillow.py` | Core script for loading, displaying, splitting RGB channels, and visualizing individual channels (red, green, blue only) | `Image.open()`, `Image.split()`, `Image.merge()`, channel zeroing, side-by-side concatenation |
| Quantization / posterization demos | Reducing grayscale levels (256 → 32, 16, 8, 4, 2) and comparing results side-by-side | `ImageOps.grayscale()`, `Image.quantize()`, bit-depth reduction effects |
| Cropping & slicing | Displaying full image, top N rows, left N columns | NumPy slicing `array[0:rows, :, :]`, `array[:, 0:columns, :]` |
| Reference vs Copy | Demonstrating how `B = A` is a reference (aliasing) vs `B = A.copy()` | NumPy `.copy()`, memory sharing, unexpected side-effects when modifying arrays |
| Channel isolation examples | Showing only red / green / blue channels (color + grayscale versions) | `array[:,:,0]`, `array.copy()`, zeroing other channels |
| Array saving & loading | Converting PIL Image → NumPy array and saving `.npy` files | `np.asarray(image)`, `np.save()`, folder creation with `os.makedirs()` |
| Helper functions | Reusable utilities like horizontal concatenation | `get_concat_h()`, side-by-side image display |

All scripts focus on the same sample image: **`cod7_25_25.png`** (a 512×512 or similar RGB/PNG file).

## Requirements

```bash
pip install pillow numpy matplotlib
