import os
from PIL import Image

# ────────────────────────────────────────────────
# Get current working directory (where THIS script is running)
cwd = os.getcwd()
print("Current script directory (cwd) :", cwd)

# Go up one level (parent folder)
parent_dir = os.path.dirname(cwd)          # cleaner than "../"
print("Parent directory              :", parent_dir)

# Define image filename (make sure exact match!)
image_filename = "cod7_25_25.png"          # ← double-check spelling & extension

# Build full path to image (one folder up)
image_path = os.path.join(parent_dir, image_filename)

print("Trying to open this path       :", image_path)
print("Path exists?                   :", os.path.exists(image_path))

# Quick debug: show what’s actually in the parent folder
print("\nFiles & folders in parent directory:")
print(os.listdir(parent_dir))

# ────────────────────────────────────────────────
if not os.path.exists(image_path):
    print("\nERROR: Image file not found!")
    print("  → Check that the file really exists in the parent folder")
    print("  → Verify exact filename (case-sensitive on some systems)")
    print("  → Make sure you're running the script from the subfolder")
    exit(1)

# Open the image
try:
    image = Image.open(image_path)
    print("\nSuccess! Image opened.")
    print("  Type:", type(image))
    print("  Mode:", image.mode)
    print("  Size:", image.size)

    # Show it
    image.show()  # opens in default viewer

    # Optional: close when done
    # image.close()

except Exception as e:
    print("\nFailed to open image:")
    print(e)

print("\nDone.")