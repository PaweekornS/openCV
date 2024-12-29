import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image/map.jpg', 0)

thres, th1 = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 1)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 1)

images = [img, th1, th2, th3]
titles = ['Original', 'classical', 'adaptive_mean', 'adaptive_gaussian']

for i, image in enumerate(images):
    plt.subplot(2, 2, i+1, xticks=[], yticks=[])
    plt.imshow(image, cmap='gray')
    plt.title(titles[i])
plt.show()
