import cv2
import numpy as np

img = cv2.imread('image/color.jpg')

def clickPosition(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        color = img[y, x]
        text = f'R:{color[2]}, G:{color[1]}, B:{color[0]}'
        
        # display text on image
        cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow("Tree", img)
        
        # display color that we clicked
        new_window = np.zeros((300, 300, 3), np.uint8)
        new_window[:] = color
        cv2.imshow("Result", new_window)

cv2.imshow("Tree", img)

# mouse event
cv2.setMouseCallback("Tree", clickPosition)

cv2.waitKey(0)
cv2.destroyAllWindows()
