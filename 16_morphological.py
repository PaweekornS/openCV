import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image/CoinNoise.png', 0)
thresh, bin_img = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((2, 2), np.uint8)
# Dilation and Erosion
dilated = cv2.dilate(bin_img, kernel, iterations=5)
erosion = cv2.erode(bin_img, kernel, iterations=5)

# Opening and Closing
opening = cv2.morphologyEx(bin_img, cv2.MORPH_OPEN, kernel, iterations=5)
closing = cv2.morphologyEx(bin_img, cv2.MORPH_CLOSE, kernel, iterations=5)

titles = ['Original', 'THRESH', 'Dilation', 'Erosion', 'Opening', 'Closing']
images = [img, bin_img, dilated, erosion, opening, closing]

for i in range(len(images)):
    plt.subplot(2, 3, i+1, xticks=[], yticks=[])
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
plt.show()
