import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the color image
color_image = cv2.imread("1.png")


# Create the negative of the color image
negative_color_image = np.abs(255 - color_image)

# Convert the color image to grayscale
grayscale_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

# Create the negative of the grayscale image
negative_grayscale_image = np.abs(255 - grayscale_image)

# Display the original, grayscale, and negative images using matplotlib
plt.figure(figsize=(8, 8))

# Original Image
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('on')

# Grayscale Image
plt.subplot(2, 2, 2)
plt.imshow(grayscale_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('on')

# Negative Grayscale Image
plt.subplot(2, 2, 3)
plt.imshow(negative_grayscale_image, cmap='gray')
plt.title('Negative Grayscale Image')
plt.axis('on')

# Negative Color Image
plt.subplot(2, 2, 4)
plt.imshow(cv2.cvtColor(negative_color_image, cv2.COLOR_BGR2RGB))
plt.title('Negative Color Image')
plt.axis('on')

plt.show()