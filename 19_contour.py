import cv2

img = cv2.imread('image/ant.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh, bin_img = cv2.threshold(gray_img, 215, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(bin_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img, contours, -1, (0, 150, 0), 3)

cv2.imshow('Output', img)
cv2.waitKey()