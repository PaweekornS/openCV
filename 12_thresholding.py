import cv2
import matplotlib.pyplot as plt

gray_img = cv2.imread('image/gradient.png')

# binary image
# normal func: value which > thresh will be set to <max_val>
thresh, bin_img = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY)
thresh, bin_inv = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY_INV)

# truncated: value which > thresh will be set to thresh
thresh, trunc_img = cv2.threshold(gray_img, 128, 255, cv2.THRESH_TRUNC)

# zero: value which < thresh will be set to 0
thresh, zero_img = cv2.threshold(gray_img, 128, 255, cv2.THRESH_TOZERO)
thresh, zero_inv = cv2.threshold(gray_img, 128, 255, cv2.THRESH_TOZERO_INV)

'''openCV approach'''
# cv2.imshow('original', gray_img)
# cv2.imshow('bin', bin_img)
# cv2.imshow('bin_inv', bin_inv)
# cv2.imshow('trunc', trunc_img)
# cv2.imshow('TOZERO', zero_img)
# cv2.imshow('TOZERO_INV', zero_inv)

# cv2.waitKey()
# cv2.destroyAllWindows()

'''Matplotlib approach'''
images = [gray_img, bin_img, bin_inv, trunc_img, zero_img, zero_inv]
title = ['original', 'binary', 'binary_inv', 'truncated', 'zero', 'zero_inv']

plt.subplots(2, 3, figsize=(12, 5))
for i, image in enumerate(images):
    plt.subplot(2, 3, i+1)
    plt.imshow(image[:, :, ::-1])
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])
plt.show()
