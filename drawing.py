import cv2 as cv

img = cv.imread('image/cat.jpg')
resize = cv.resize(img,(600,600))

point = []
def ConnectPoint(event,x,y,flags,params):
    if event is cv.EVENT_LBUTTONDOWN:
        cv.circle(resize,(x,y),10,(0,0,255),4)
        point.append((x,y))
        if len(point) >= 2 :
             cv.line(resize,point[-2],point[-1],(0,255,0),5)
        cv.imshow('output',resize)
        
cv.imshow('output',resize)
cv.setMouseCallback('output',ConnectPoint)
cv.waitKey(0)
cv.destroyAllWindows()
