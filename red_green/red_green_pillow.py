import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

# ────────────────────────────────────────────────
# 1. Define the filename (adjust path if image is not in current folder)
filename = "../cod7_25_25.png"
full_path = os.path.join(os.getcwd(), filename)

# Debug: check existence
if not os.path.exists(full_path):
    print(f"File not found: {full_path}")
    print("Files in current folder:", os.listdir(os.getcwd()))
    # If not found → either move the file or fix the path
    # Example absolute path (uncomment & adjust if needed):
    # full_path = r"C:\Users\jumpk\github\python-scripts\cod7_25_25.png"
    raise FileNotFoundError(f"Cannot find {filename}")

# ────────────────────────────────────────────────
# 2. Load image → convert to NumPy array
img = Image.open(full_path)
array = np.array(img)

print(f"Loaded image: {filename}")
print(f"  Shape: {array.shape}  (height, width, channels)")
print(f"  Data type: {array.dtype}")

# Make a copy so we don't modify the original array
blue_array = array.copy()

# Zero out red ([:,:,0]) and green ([:,:,1]) → keep only blue channel
blue_array[:, :, 0] = 0   # red = 0
blue_array[:, :, 1] = 0   # green = 0
# blue_array[:, :, 2] remains unchanged → blue values stay

# ────────────────────────────────────────────────
# 3. Display
plt.figure(figsize=(10, 10))
plt.imshow(blue_array)
plt.title("Image with only blue channel visible\n(Red & Green set to 0)")
plt.axis('off')

# Option A: Show interactively (best in Jupyter / interactive shells)
plt.show()

# Option B: Save to file (reliable in plain .py scripts on Windows/macOS)
plt.savefig("cod7_only_blue_channel.png", dpi=120, bbox_inches='tight')
print("Saved result as: cod7_only_blue_channel.png")

# Optional: also show original for comparison
plt.figure(figsize=(10, 10))
plt.imshow(array)
plt.title("Original image")
plt.axis('off')
plt.savefig("cod7_original.png", dpi=120, bbox_inches='tight')
print("Saved original as: cod7_original.png")

plt.close('all')  # free memory