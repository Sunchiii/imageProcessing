import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ref,frame = cap.read()#ref is boolean status read image#frame is image
    cv.imshow('openVideo',frame)
    if cv.waitKey(1) and 0xFF == ord("e"):
        break
cap.release()
cv.destroyAllWindows()
    
