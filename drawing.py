import cv2 as cv

img = cv.imread('image/cat.jpg')
resize = cv.resize(img,(600,600))

#draw line/ arrow  param
#line(image , (start position x,y),(end position x,y),(color BGR),thickness 10)
cv.line(resize,(400,50),(200,500),(255,0,0),10)
cv.imshow('output',resize)
cv.waitKey(0)
cv.destroyAllWindows()
