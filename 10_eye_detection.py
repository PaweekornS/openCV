import cv2

'''image'''
# img = cv2.imread('image/girl.jpg')

# eye_cascade = cv2.CascadeClassifier('Detect/haarcascade_eye_tree_eyeglasses.xml')

# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# eye_detect = eye_cascade.detectMultiScale(gray_img)

# for (x, y, w, h) in eye_detect:
#     cv2.rectangle(img, (x, y), (x+w, y+h), color=(0, 255, 0), thickness=3)

# cv2.imshow('Original', img)


'''Video'''
cap = cv2.VideoCapture('image/Mark.mp4')
eye_cascade = cv2.CascadeClassifier('Detect/haarcascade_eye_tree_eyeglasses.xml')

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        eye_detect = eye_cascade.detectMultiScale(gray_frame)
        
        for (x, y, w, h) in eye_detect:
            cv2.rectangle(frame, (x, y), (x+w, y+h), 
                          color=(0, 255, 0), thickness=3)
            
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break
        
        cv2.imshow("Original", frame)
        
    else:
        break


cv2.waitKey()
cv2.destroyAllWindows()