import cv2

img = cv2.imread('image/cat.jpg')

img_resize = cv2.resize(img, (700, 700))

''' draw lines: color in cv2 is read in BGR order; color dtype in cv2: uint8 (0-255)'''
# cv2.line(img_resize, (0, 0), (700, 700), (0, 100, 0), 2)
# cv2.arrowedLine(img_resize, (0, 0), (200, 300), (0, 0, 255), 2)

'''rectangle
Note: thickness = -1 means fill the shape'''
# cv2.rectangle(img_resize, (0, 0), (200, 300), (200, 0, 0), -1)

'''circle'''
# cv2.circle(img_resize, (400, 50), 30, (200, 150, 0), 5)

'''text'''
cv2.putText(img_resize, "Cat", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 150), 5, cv2.LINE_AA)

cv2.imshow("Cat", img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()