import cv2 as cv
import numpy as np

while True:
    img = cv.imread('image/bottleCap.jpg')
    img = cv.resize(img,(400,400))
    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

    #min and max color of object
    green_upper = np.array([0, 139, 0])
    green_lower = np.array([0, 116, 23])

    mask = cv.inRange(hsv,green_lower,green_upper)
    result = cv.bitwise_and(hsv,hsv,mask=mask)
   if cv.waitKey(0) & 0xFF == ord('e'):
       break
   cv.imshow('original',img)
   cv.imshow('Mask',mask)
   cv.imshow('Result',result)
   
cv.destroyAllWindows()
