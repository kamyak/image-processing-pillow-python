import os
from PIL import Image

def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

# ────────────────────────────────────────────────
print("Python version:", sys.version.split()[0] if 'sys' in globals() else "unknown")
print("Current working directory:", os.getcwd())
print("Script file location (if running as file):", os.path.abspath(__file__) if '__file__' in globals() else "interactive session")

output_folder = "rgb"
full_output_path = os.path.join(os.getcwd(), output_folder)
print(f"Will try to create/save in: {full_output_path}")

# Create folder with check
try:
    os.makedirs(output_folder, exist_ok=True)
    print(f"Folder '{output_folder}' ready (exists or created)")
except Exception as e:
    print(f"Failed to create folder: {e}")
    exit(1)

my_image = "../cod7_25_25.png"
image_path = os.path.join(os.getcwd(), my_image)

if not os.path.exists(image_path):
    print(f"ERROR: Image not found at {image_path}")
    print("Files in current folder:", os.listdir('.'))
    exit(1)

print(f"Image found: {image_path}")

with Image.open(image_path) as image:
    print("Image opened successfully")
    red, green, blue = image.split()
    zero = Image.new('L', red.size, 0)

    red_vis   = Image.merge('RGB', (red,   zero, zero))
    green_vis = Image.merge('RGB', (zero, green, zero))
    blue_vis  = Image.merge('RGB', (zero, zero, blue))

    combined_red   = get_concat_h(image, red_vis)
    combined_green = get_concat_h(image, green_vis)
    combined_blue  = get_concat_h(image, blue_vis)

    # Save with confirmation
    red_path   = os.path.join(output_folder, "original_vs_red.png")
    green_path = os.path.join(output_folder, "original_vs_green.png")
    blue_path  = os.path.join(output_folder, "original_vs_blue.png")

    combined_red.save(red_path)
    print(f"Saved:   {red_path}")

    combined_green.save(green_path)
    print(f"Saved:   {green_path}")

    combined_blue.save(blue_path)
    print(f"Saved:   {blue_path}")

    # Show (optional)
    combined_red.show(title="Original + Red channel")
    combined_green.show(title="Original + Green channel")
    combined_blue.show(title="Original + Blue channel")

print("Script finished.")
print("Check folder:", full_output_path)
print("Files should now be:", os.listdir(output_folder) if os.path.exists(output_folder) else "folder still missing")