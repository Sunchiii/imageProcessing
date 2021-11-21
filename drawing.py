import cv2 as cv

img = cv.imread('image/cat.jpg')
resize = cv.resize(img,(600,600))

#draw rectangle
#rectangle(image , (top,left),(bottom,right),(BGR),5)
cv.rectangle(resize,(50,50),(200,200),(255,0,0),5)
cv.imshow('output',resize)
cv.waitKey(0)
cv.destroyAllWindows()
