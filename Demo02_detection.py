import cv2

'''Image'''
# img = cv2.imread('image/girl.jpg')
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # face detection
# face_cascade = cv2.CascadeClassifier('Detect/haarcascade_frontalface_default.xml')
# face_detect = face_cascade.detectMultiScale(img_gray, minNeighbors=5)

# for (x, y, w, h) in face_detect:
#     cv2.rectangle(img, (x, y), (x+w, y+h),
#                   color=(0, 255, 0), thickness=5)

# # eye detection
# eye_cascade = cv2.CascadeClassifier('Detect/haarcascade_eye_tree_eyeglasses.xml')
# eye_detect = eye_cascade.detectMultiScale(img_gray)
    
# for (x, y, w, h) in eye_detect:
#     cv2.rectangle(img, (x, y), (x+w, y+h),
#                   color=(255, 0, 0), thickness=5)

# # display image
# cv2.imshow("Original", img)
# cv2.waitKey()
# cv2.destroyAllWindows()


'''Video'''
cap = cv2.VideoCapture('image/Mark.mp4')

face_cascade = cv2.CascadeClassifier('Detect/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('Detect/haarcascade_eye_tree_eyeglasses.xml')

def display_detected(frame):
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    face_detect = face_cascade.detectMultiScale(gray_img)
    for (x, y, w, h) in face_detect:
        cv2.rectangle(frame, (x, y), (x+w, y+h),
                      (0, 255, 0), 3)
        
    eye_detect = eye_cascade.detectMultiScale(gray_img)
    for(x, y, w, h) in eye_detect:
        cv2.rectangle(frame, (x, y), (x+w, y+h),
                      (255, 0, 0), 5)


while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        display_detected(frame)
        cv2.imshow('original', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()
