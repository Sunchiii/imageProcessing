import cv2 as cv

img = cv.imread('square.png',0)
print(img.ndim)#show image
cv.imshow('show image gray color',img)
cv.waitKey(delay=10000)#show image 10sec if is 0 maen show without time
cv.destroyAllWindows()
