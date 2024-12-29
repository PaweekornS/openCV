import cv2
import numpy as np

cap = cv2.VideoCapture('image/Walking.mp4')


'''My appraoch: adjusting threshold only'''
# def detect_contour(frame):
#     gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     thresh, bin_img = cv2.threshold(gray_img, 100, 255, cv2.THRESH_BINARY)

#     contours, hierarchy = cv2.findContours(bin_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

#     cv2.drawContours(frame, contours, -1, (0, 150, 0), 3)
    
# while(cap.isOpened()):
#     ret, frame = cap.read()
    
#     if ret == True:
#         detect_contour(frame)
#         cv2.imshow('frame', frame)
        
#         if cv2.waitKey(1) & 0xFF == ord('e'):
#             break
#     else:
#         break

'''Advanced technique
1. find the different in the consecutive frame
2. use gaussian blur to reduce noise
3. dilate the edge of the object'''

def expand_contour(frame1, frame2):
    motion_diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(motion_diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thres, bin_img = cv2.threshold(blur, 15, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(bin_img, None, iterations=3)
    
    return dilated
    

ret, frame1 = cap.read()
ret, frame2 = cap.read()
while(cap.isOpened()):
    if ret == True:
        frame = expand_contour(frame1, frame2)
        
        # contour detection
        contours, hierarchy = cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        
        # draw rectangle
        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            if cv2.contourArea(contour) < 2500:
                continue
            
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 150, 0), 2)
        cv2.imshow('Output', frame1)
        
        # set frame1 to next frame for continuing the video
        frame1 = frame2
        ret, frame2 = cap.read()
        if cv2.waitKey(10) & 0xFF == ord('e'):
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()
