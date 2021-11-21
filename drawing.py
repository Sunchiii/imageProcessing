import cv2 as cv

img = cv.imread('image/cat.jpg')
resize = cv.resize(img,(600,600))

#draw text
#cv.putText(image,'text',(position x,y),font#hersheyfontOnOpemcv,font scale,(color BGR),bold)
cv.putText(resize,'this is a cat',(10,50),1,4,(0,0,0))
cv.imshow('output',resize)
cv.waitKey(0)
cv.destroyAllWindows()
