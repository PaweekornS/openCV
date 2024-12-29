import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()  # receive picture from camera frame by frame
    cv2.imshow('Output', frame)
    
    # exit when press('e')
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv2.destroyAllWindows()
