import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


img = Image.open("1.jpg")
M = np.asarray(img)

red_channel = M[:, :, 0]
green_channel = M[:, :, 1]
blue_channel = M[:, :, 2]

red_enhanced = np.clip(red_channel * 1.5, 0, 255)  
green_enhanced = np.clip(green_channel * 1.5, 0, 255)
blue_enhanced = np.clip(blue_channel * 1.5, 0, 255)

enhanced_image = np.stack((red_enhanced, green_channel, blue_channel), axis=-1).astype(np.uint8)
enhanced_image = Image.fromarray(enhanced_image)

enhanced_image1 = np.stack((red_channel, green_enhanced, blue_channel), axis=-1).astype(np.uint8)
enhanced_image1 = Image.fromarray(enhanced_image1)

enhanced_image2 = np.stack((red_channel, green_channel, blue_enhanced), axis=-1).astype(np.uint8)
enhanced_image2 = Image.fromarray(enhanced_image2)

plt.figure(figsize=(12, 6))

plt.subplot(1, 4, 1)
plt.imshow(img)
plt.title("Original Image")

plt.subplot(1, 4, 2)
plt.imshow(enhanced_image)
plt.title("Enhanced Image (Red Channel)")

plt.subplot(1, 4, 3)
plt.imshow(enhanced_image1)
plt.title("Enhanced Image (Green Channel)")

plt.subplot(1, 4, 4)
plt.imshow(enhanced_image2)
plt.title("Enhanced Image (Blue Channel)")

plt.show()