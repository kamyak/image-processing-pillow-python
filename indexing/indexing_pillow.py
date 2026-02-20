import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# ────────────────────────────────────────────────
# 1. Load your image
image_path = "../cod7_25_25.png"  # adjust if needed (e.g. "cod7_25_25.png" or full absolute path)

if not os.path.exists(image_path):
    print(f"Error: {image_path} not found!")
    print("Files in current directory:", os.listdir("."))
    print("Tip: If the image is one folder up, keep '../'. If same folder, remove '../'.")
    exit(1)

img = Image.open(image_path)
array = np.array(img)
print(f"Loaded {image_path}")
print(f"  Shape: {array.shape}  (height, width, channels)")
print(f"  Data type: {array.dtype}")

# ────────────────────────────────────────────────
def save_and_show(fig_name):
    """Helper: save figure + optional interactive show"""
    plt.savefig(f"{fig_name}.png", dpi=120, bbox_inches='tight')
    print(f"Saved: {fig_name}.png")
    # plt.show()          # uncomment for interactive pop-ups
    # plt.show(block=True)
    plt.close()           # free memory

# ────────────────────────────────────────────────
# Full image
plt.figure(figsize=(10, 10))
plt.imshow(array)
plt.title("Full Image – cod7_25_25")
plt.axis('off')
save_and_show("cod7_full_image")

# Top 256 rows
rows = 256
plt.figure(figsize=(10, 10))
plt.imshow(array[0:rows, :, :])
plt.title(f"Top {rows} rows – cod7_25_25")
plt.axis('off')
save_and_show("cod7_top_256_rows")

# Left 256 columns
columns = 256
plt.figure(figsize=(10, 10))
plt.imshow(array[:, 0:columns, :])
plt.title(f"Left {columns} columns – cod7_25_25")
plt.axis('off')
save_and_show("cod7_left_256_columns")

# ────────────────────────────────────────────────
# Reference vs Copy demo
A = array.copy()          # independent copy
B = A                     # B is just another name for the same array
A[:, :, :] = 0            # zeroing A also affects B

plt.figure(figsize=(8, 8))
plt.imshow(B)
plt.title("B after A[:,:,:]=0  (shows that B is a reference, not a copy)")
plt.axis('off')
save_and_show("cod7_reference_vs_copy_demo_all_black")

# Reset for next demos
A = array.copy()

# ────────────────────────────────────────────────
# Channel isolation examples (using the same image)

# Red channel only
red_only = array.copy()
red_only[:, :, 1] = 0     # zero green
red_only[:, :, 2] = 0     # zero blue
plt.figure(figsize=(10, 10))
plt.imshow(red_only)
plt.title("cod7_25_25 – Red channel only")
plt.axis('off')
save_and_show("cod7_red_only")

# Green channel only
green_only = array.copy()
green_only[:, :, 0] = 0
green_only[:, :, 2] = 0
plt.figure(figsize=(10, 10))
plt.imshow(green_only)
plt.title("cod7_25_25 – Green channel only")
plt.axis('off')
save_and_show("cod7_green_only")

# Blue channel only
blue_only = array.copy()
blue_only[:, :, 0] = 0
blue_only[:, :, 1] = 0
plt.figure(figsize=(10, 10))
plt.imshow(blue_only)
plt.title("cod7_25_25 – Blue channel only")
plt.axis('off')
save_and_show("cod7_blue_only")

# Red channel in grayscale
plt.figure(figsize=(10, 10))
plt.imshow(array[:, :, 0], cmap='gray')
plt.title("cod7_25_25 – Red channel (grayscale)")
plt.axis('off')
save_and_show("cod7_red_grayscale")

print("\nAll figures saved as PNG files in the current folder.")
print("Files created:")
print("  cod7_full_image.png")
print("  cod7_top_256_rows.png")
print("  cod7_left_256_columns.png")
print("  cod7_reference_vs_copy_demo_all_black.png")
print("  cod7_red_only.png")
print("  cod7_green_only.png")
print("  cod7_blue_only.png")
print("  cod7_red_grayscale.png")
print("\nOpen them to compare the results.")