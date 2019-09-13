import numpy as np
import cv2


#this is the cascade we just made. Call what you want
object_cascade = cv2.CascadeClassifier('cascade.xml')

cap = cv2.VideoCapture('/home/insanesac/workspace/Fitvity/elete_raw_video.mp4')

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # add this
    # image, reject levels level weights.
    object1 = object_cascade.detectMultiScale(gray, 50, 50)
    print(object1)
    # add this
    for (x,y,w,h) in object1:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()