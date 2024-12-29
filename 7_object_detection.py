import cv2
import numpy as np


while(True):
    img = cv2.imread('image/ball2d.jpg', 1)
    img = cv2.resize(img, (400, 400))
    cv2.imshow("ball", img)
    
    # detect color range (BGR), color value needs to be obtained first
    lower = np.array([5, 111, 10])
    upper = np.array([124, 255, 133])
    
    mask = cv2.inRange(img, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)
    
    if cv2.waitKey(0):
        break

cv2.destroyAllWindows()
