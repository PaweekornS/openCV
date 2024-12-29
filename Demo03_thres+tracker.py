import cv2

def display(value):
    pass

cv2.namedWindow('Output')
cv2.createTrackbar('value', 'Output', 128, 255, display)

while True:
    gray_img = cv2.imread('image/ant.jpg', 0)
    thresh_val = cv2.getTrackbarPos('value', 'Output')
    thresh, cvt_img = cv2.threshold(gray_img, thresh_val, 255, cv2.THRESH_BINARY)
    
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break
    
    cv2.imshow('Output', cvt_img)
    
cv2.destroyAllWindows()
