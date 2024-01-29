import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


img = Image.open("1.jpg")
M = np.asarray(img)

red_channel = M[:, :, 0]
green_channel = M[:, :, 1]
blue_channel = M[:, :, 2]

red_enhanced = np.clip(red_channel * 2, 0, 255)  
enhanced_image = np.stack((red_enhanced, green_channel, blue_channel), axis=-1).astype(np.uint8)
enhanced_image = Image.fromarray(enhanced_image)

plt.figure(figsize=(8, 8))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(enhanced_image)
plt.title("Enhanced Image (Red Channel)")

plt.show()