import numpy as np
from PIL import Image
import os

# ────────────────────────────────────────────────
my_image = "cod7_25_25.png"
image_path = os.path.join(os.getcwd(), my_image)

# Check if file exists
if not os.path.exists(image_path):
    print(f"File not found: {image_path}")
    print("Files in current folder:", os.listdir(os.getcwd()))
    exit(1)

# ────────────────────────────────────────────────
# Open the image
try:
    image = Image.open(image_path)
    print("Image opened successfully")
    print("  Mode:       ", image.mode)     # should be 'RGB' or 'RGBA'
    print("  Size:       ", image.size)     # (width, height)
    print("  Format:     ", image.format)
except Exception as e:
    print(f"Error opening image: {e}")
    exit(1)

# Convert to NumPy array
array = np.asarray(image)

# ────────────────────────────────────────────────
print("\nNumPy array info:")
print("  Type:            ", type(array))          # <class 'numpy.ndarray'>
print("  Shape:           ", array.shape)         # e.g. (height, width, 3)
print("  Data type:       ", array.dtype)       # usually uint8
print("  Total elements:  ", array.size)
print("  Memory usage:    ", f"{array.nbytes / 1024 / 1024:.2f} MB")

# Pixel access examples
print("\nPixel at top-left corner [row=0, col=0]:", array[0, 0])          # [R, G, B]
print("Pixel at [row=10, col=20]:                 ", array[10, 20])

# Statistics
print("\nStatistics:")
print("  Min value (all channels):", array.min())
print("  Max value (all channels):", array.max())
print("  Mean value:              ", f"{array.mean():.2f}")

# Small preview
if array.shape[0] > 10 or array.shape[1] > 10:
    print("\nTop-left 5×5 pixels (RGB):")
    print(array[:5, :5])
else:
    print("\nFull array (small image):")
    print(array)

# ────────────────────────────────────────────────
# Save the array
output_folder = "arrays"
os.makedirs(output_folder, exist_ok=True)

# Use original filename without extension
base_name = os.path.splitext(my_image)[0]  # → "cod7_25_25"
save_path = os.path.join(output_folder, f"{base_name}_array.npy")

np.save(save_path, array)
print(f"\nArray saved successfully to:")
print(f"  {save_path}")
print(f"  Shape preserved: {array.shape}")
print(f"  File size approx: {os.path.getsize(save_path) / 1024 / 1024:.2f} MB")

# Optional: save individual channels (uncomment if needed)
# np.save(os.path.join(output_folder, f"{base_name}_red.npy"),   array[:,:,0])
# np.save(os.path.join(output_folder, f"{base_name}_green.npy"), array[:,:,1])
# np.save(os.path.join(output_folder, f"{base_name}_blue.npy"),  array[:,:,2])
# print("Individual channels also saved.")

# ────────────────────────────────────────────────
# Clean up
image.close()
print("\nDone.")