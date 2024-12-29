import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
points = []

'''Create point when clicked, if more than 2 points create a connection line'''
def clickPosition(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 10, (0, 0, 255), 3)
        points.append((x, y))
        # print(points)
        
        if len(points) >= 2:
            cv2.arrowedLine(img, points[-2], points[-1], (255, 0, 0), 2)
            
        cv2.imshow("Tree", img)

cv2.imshow("Tree", img)

cv2.setMouseCallback("Tree", clickPosition)
cv2.waitKey()
cv2.destroyAllWindows()
