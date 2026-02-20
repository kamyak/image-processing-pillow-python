import os
from PIL import Image
import matplotlib.pyplot as plt

cwd = os.getcwd()
print("Current directory:", cwd)

# Import image
my_image = "../cod7_25_25.png"

# Image path
image_path = os.path.join(cwd, my_image)
print("Trying to open:", image_path)

# Open image
image = Image.open(image_path)

# Image type
print("Image type:", type(image))

# Image size
print("Image size:", image.size)

# Image mode type
print("Image mode:", image.mode)

# Image intensity on x and y 
im = image.load() 
x = 0
y = 1
print("X=", x)
print("Y=", y)
print("Image intensity on x and y", im[y,x])

# Plot image in your default image viewer
plt.figure(figsize=(10,10))
plt.imshow(image)
plt.show()

# Save the image
image.save("plotted_cod7_25_25.jpg")