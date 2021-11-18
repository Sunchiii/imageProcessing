import cv2 as cv

img = cv.imread('square.png',0)
print(img.ndim)#show image
width = int(img.shape[0]*80/100)
hieght = int(img.shape[1]*80/100)
dim = (width,hieght)
resize = cv.resize(img,dim)
cv.imwrite('gray.jpg',resize)
cv.imshow('show image gray color',resize)
cv.waitKey(delay=10000)#show image 10sec if is 0 maen show without time
cv.destroyAllWindows()
