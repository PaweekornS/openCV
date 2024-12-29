import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')

result = cv2.VideoWriter("output.avi", fourcc, 60, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read() 
    
    if ret == True:
        cv2.imshow('Output', frame)
        result.write(frame)
        if cv2.waitKey(10) & 0xFF == ord("e"):
            break

result.release()
cap.release()
cv2.destroyAllWindows()
