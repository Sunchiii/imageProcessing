import cv2 as cv

img = cv.imread('image/tree.jpg')

def showposition(event,x,y,flags,params):
    if event == cv.EVENT_LBUTTONDOWN:
       blue = img[y,x,0]#[position x,position y,index color 0|1|3]
       green = img[y,x,1]
       red = img[y,x,2]
       text = str(blue)+'.'+str(green)+'.'+str(red)
       cv.putText(img,text,(x,y),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),cv.LINE_4) 
       cv.imshow('output',img)

cv.imshow('output',img)
cv.setMouseCallback('output',showposition)#(discription,funtion)
cv.waitKey(0)
cv.destroyAllWindows()
