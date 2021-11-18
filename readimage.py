import cv2 as cv

img = cv.imread('square.png',1)
print(img.ndim)
cv.waitKey(0)
cv.destroyAllWindows()
