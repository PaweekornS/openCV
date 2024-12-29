import cv2
import datetime

cap = cv2.VideoCapture('image/video.mp4')

while (cap.isOpened()):
    ret, frame = cap.read()
    
    # check is video ended
    if ret == True:
        current_date = str(datetime.datetime.now())
        cv2.putText(frame, current_date, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 5, cv2.LINE_4)
        
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Output", frame)
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()
    