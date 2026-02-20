import os
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

def get_concat_h(im1, im2):
    # Assumes both images have same height
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

cwd = os.getcwd()
print("Current directory:", cwd)

my_image = "../cod7_25_25.png"
image_path = os.path.join(cwd, my_image)
print("Trying to open:", image_path)

# ── Open the original image ────────────────────────────────
original = Image.open(image_path)
print("Original mode:", original.mode)
print("Original size:", original.size)

# Convert to grayscale once (mode 'L')
image_gray = ImageOps.grayscale(original)
print("Grayscale mode:", image_gray.mode)

# Optional: show the grayscale version
# image_gray.show(title="Grayscale version")

# Create output folder if it doesn't exist
output_dir = "quantized"
os.makedirs(output_dir, exist_ok=True)   # won't error if folder already exists

# ── Compare different quantization levels ──────────────────
for n in range(3, 8):
    levels = 256 // (2 ** n)
    # Quantize the grayscale image
    quantized = image_gray.quantize(levels)
    
    # Convert both to RGB so they can be concatenated side-by-side
    left  = image_gray.convert('RGB')
    right = quantized.convert('RGB')
    
    combined = get_concat_h(left, right)
    
    # Matplotlib display
    plt.figure(figsize=(12, 7))
    plt.imshow(combined)
    plt.title(f"Original Grayscale (256 levels)  vs  {levels} levels (quantized)")
    plt.axis("off")
    
    # Save each comparison (recommended for scripts)
    save_path = os.path.join(output_dir, f"quantization_{levels}_levels.png")
    plt.savefig(save_path, dpi=140, bbox_inches='tight')
    print(f"Saved: {save_path}")
    
    # Show interactively (uncomment if you prefer pop-ups)
    plt.show()

    # Close figure to free memory
    plt.close()

print("Done. Check the saved PNG files in your folder.")