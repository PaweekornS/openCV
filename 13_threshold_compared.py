import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image/ant.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh_val = [50, 100, 130, 200, 230]

plt.subplot(231, xticks=[], yticks=[])
plt.imshow(gray_img, cmap='gray')
plt.title('Original')

for i, thresh in enumerate(thresh_val):
    thresh, cvt_img = cv2.threshold(gray_img, thresh, 255, cv2.THRESH_BINARY)
    plt.subplot(2, 3 , i+2, xticks=[], yticks=[])
    plt.title(f'Threshold: {thresh}')
    plt.imshow(cvt_img, cmap='gray')
plt.show()