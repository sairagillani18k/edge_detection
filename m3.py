from PIL import Image, ImageFilter
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Open the image
image = Image.open("pic1.png")

# Convert the image to grayscale
image_gray = image.convert("L")

# Detect edges using the FIND_EDGES filter
edges_image = image_gray.filter(ImageFilter.FIND_EDGES)

# Convert the edges-detected image to a NumPy array
edges_array = np.array(edges_image)

# Convert the edges image to an HSV image
edges_hsv = cv2.cvtColor(edges_array, cv2.COLOR_GRAY2BGR)
edges_hsv = cv2.cvtColor(edges_hsv, cv2.COLOR_BGR2HSV)

# Create masks for unsaturated and bright regions
unsat_mask = edges_hsv[:, :, 1] < 50
bright_mask = edges_hsv[:, :, 2] > 240

# Combine the masks to identify white or bright regions
white_mask = (unsat_mask & bright_mask).astype(np.uint8) * 255

# Apply the mask to the original image
filtered_wires = cv2.bitwise_and(np.array(image), np.array(image), mask=white_mask)

# Save the image using PIL
filtered_pil_image = Image.fromarray(filtered_wires)
filtered_pil_image.save('filtered.png')

# Display the results
plt.subplot(1, 2, 1)
plt.imshow(np.array(image))
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(filtered_wires[:, :, ::-1])  # Convert BGR to RGB for display
plt.title('Filtered Wires')

plt.tight_layout()
plt.show()
