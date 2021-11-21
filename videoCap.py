import cv2 as cv
import datetime as time

cap = cv.VideoCapture(0)

while cap.isOpened():
    ref,frame = cap.read()#ref is boolean status read image#frame is image

    if ref is True:
        currentDate = str(time.datetime.now())
        cv.putText(frame,currentDate,(10,30),cv.FONT_HERSHEY_SIMPLEX,0.8,(0,0,0),cv.LINE_4)
        cv.imshow('openVideo',frame)
    else:
        break
    if cv.waitKey(1) and 0xFF == ord("e"):
        break
cap.release()
cv.destroyAllWindows()
    
