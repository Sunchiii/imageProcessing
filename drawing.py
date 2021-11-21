import cv2 as cv

img = cv.imread('image/cat.jpg')
resize = cv.resize(img,(600,600))

#draw circle
#cv.circle(image,(center point x,y),scale,(color BGR),border)
cv.circle(resize,(426,349),100,(0,255,0),5)
cv.imshow('output',resize)
cv.waitKey(0)
cv.destroyAllWindows()
