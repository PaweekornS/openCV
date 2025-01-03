import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image/map.jpg', 0)

block_size = [3, 5, 9, 17, 33]

plt.subplot(231, xticks=[], yticks=[])
plt.imshow(img, cmap='gray')
plt.title("Original")

for i, block in enumerate(block_size):
    result = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block, 1)
    plt.subplot(2, 3, i+2, xticks=[], yticks=[])
    plt.imshow(result, cmap='gray')
    plt.title(f'block: {block}')
plt.show()
