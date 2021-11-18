import cv2 as cv

img = cv.imread('square.png',0)
print(img.ndim)#show image
cv.imshow('show image gray color',img)
cv.waitKey(0)
cv.destroyAllWindows()
