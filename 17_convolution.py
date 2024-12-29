import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image/noise.png')
kernel = np.ones((3, 3), np.float32) / 9

'''Convolution
ddepth = -1 to use our original img as reference
In classical image, it's used for filter noise'''
convoluted = cv2.filter2D(img, -1, kernel)

# mean filtering (blur)
mean_blur = cv2.blur(img, (5, 5))

# median filtering
med_blur = cv2.medianBlur(img, 5)

# gaussian blur
gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)

titles = ['Original', 'Filter2D', 'Mean', 'Med', 'Gaussian']
images = [img, convoluted, mean_blur, med_blur, gaussian_blur]

for i in range(len(titles)):
    plt.subplot(2, 3, i+1, xticks=[], yticks=[])
    plt.imshow(images[i])
    plt.title(titles[i])

plt.show()