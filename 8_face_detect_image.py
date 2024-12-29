import cv2

img = cv2.imread('image/boy.jpg')

# read xml file for classification
face_cascade = cv2.CascadeClassifier('Detect/haarcascade_frontalface_default.xml')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# face classification
scaleFactor = 1.2  # scale picture e.g. 1.1 = decrease image scale 10%
minNeighbor = 2  # thresholding for detecting grayscale
face_detect = face_cascade.detectMultiScale(gray_img, scaleFactor, minNeighbor)

# show detected area
for (x, y, w, h) in face_detect:
    cv2.rectangle(img, (x, y), (x+w, y+h), 
                  color=(0, 255, 0), thickness=5)

# display
cv2.imshow("Original", img)
cv2.waitKey()
cv2.destroyAllWindows()\
