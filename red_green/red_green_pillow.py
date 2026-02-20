import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

# ────────────────────────────────────────────────
# 1. Define the filename (adjust path if needed)
filename = "../cod7_25_25.png"          # ← change to "cod7_25_25.png" if in same folder

full_path = os.path.join(os.getcwd(), filename)

# Debug: check existence
if not os.path.exists(full_path):
    print(f"File not found: {full_path}")
    print("Files in current folder:", os.listdir(os.getcwd()))
    print("\nPossible fixes:")
    print("  - Move the image to the current folder and remove '../' from filename")
    print("  - Or use absolute path, e.g.:")
    print("    full_path = r'C:\\Users\\jumpk\\github\\python-scripts\\cod7_25_25.png'")
    raise FileNotFoundError(f"Cannot find image: {filename}")

# ────────────────────────────────────────────────
# 2. Load image → convert to NumPy array
img = Image.open(full_path)
array = np.array(img)

print(f"Loaded image: {filename}")
print(f"  Shape: {array.shape}  (height, width, channels)")
print(f"  Data type: {array.dtype}")

# Make a copy so we don't modify the original
rg_array = array.copy()

# Zero out blue channel → keep only red and green
rg_array[:, :, 2] = 0   # blue = 0
# red[:,:,0] and green[:,:,1] remain unchanged

# ────────────────────────────────────────────────
# 3. Display & Save
# Red + Green only
plt.figure(figsize=(10, 10))
plt.imshow(rg_array)
plt.title("Image with only Red + Green channels visible\n(Blue set to 0)")
plt.axis('off')

# Save result
plt.savefig("cod7_red_green_only.png", dpi=120, bbox_inches='tight')
print("Saved result as: cod7_red_green_only.png")

# Show interactively (uncomment if running in Jupyter or interactive environment)
# plt.show()

# Original image for comparison
plt.figure(figsize=(10, 10))
plt.imshow(array)
plt.title("Original image")
plt.axis('off')
plt.savefig("cod7_original.png", dpi=120, bbox_inches='tight')
print("Saved original as: cod7_original.png")

# Clean up
plt.close('all')

print("\nDone. Check the saved PNG files in your current directory.")