import cv2
import matplotlib.pyplot as plt

# cv2.imread(path, flags)
# flags: 0=grayScale, 1=RGB, -1=RGB+alpha
img = cv2.imread('image/cat.jpg', 0)
img = cv2.resize(img, (500, 500))

cv2.imwrite('cat_gray.jpg', img)

cv2.imshow("Output", img)
cv2.waitKey(0)  # 5000 ms
cv2.destroyAllWindows()


