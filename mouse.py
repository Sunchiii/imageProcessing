import cv2 as cv
import numpy as np
img = cv.imread('image/tree.jpg')

def readposition(event,x,y,flags,params):
    if event == cv.EVENT_LBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]

    
        imgcolor = np.zeros([300,300,3],np.uint8)#[width,hieght,color index],numpy.uint8
        imgcolor[:] = [blue,green,red]
        cv.imshow('result',imgcolor)



cv.imshow('output',img)
cv.setMouseCallback('output',readposition)
cv.waitKey(0)
cv.destroyAllWindows()
