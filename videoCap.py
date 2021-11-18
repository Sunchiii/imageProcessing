import cv2 as cv

cap = cv.VideoCapture('image/Video.mp4')

while cap.isOpened():
    ref,frame = cap.read()#ref is boolean status read image#frame is image
    if ref is True:
        cv.imshow('openVideo',frame)
    else:
        break
    if cv.waitKey(1) and 0xFF == ord("e"):
        break
cap.release()
cv.destroyAllWindows()
    
