import cv2

'''Detect Face in video'''
cap = cv2.VideoCapture('image/Video.mp4')

face_cascade = cv2.CascadeClassifier("Detect/haarcascade_frontalface_default.xml")

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # face detection
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_detect = face_cascade.detectMultiScale(gray_img, 1.2, 5)
        for (x, y, w, h) in face_detect:
            cv2.rectangle(frame, (x, y), (x+w, y+h), 
                        color=(0, 255, 0), thickness=5)
            
        # display
        cv2.imshow("Output", frame)
        if cv2.waitKey(10) & 0xFF == ord('e'):
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows() 
