import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image/currency.jpg', 0)

# Sobel method
sobel_x = cv2.Sobel(img, -1, 1, 0)
sobel_y = cv2.Sobel(img, -1, 0, 1)
sobel = cv2.bitwise_or(sobel_x, sobel_y)

# Laplacian
laplace = cv2.Laplacian(img, -1)

# Canny
canny = cv2.Canny(img, 100, 200)

images = [img, sobel, laplace, canny]
titles = ['Original', 'Sobel', 'Laplacian', 'Canny']

for i in range(len(images)):
    plt.subplot(2, 2, i+1, xticks=[], yticks=[])
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
plt.show()
