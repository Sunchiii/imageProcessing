import cv2 as cv

cap = cv.VideoCapture(0)
four_cc = cv.VideoWriter_fourcc(*'XVID')#type of record video
result = cv.VideoWriter('grayVideo.avi',four_cc,20.0,(600,600))

while cap.isOpened():
    ref,frame = cap.read()#ref is boolean status read image#frame is image

    if ref is True:
        cv.imshow('openVideo',frame)
        result.write(frame)
    else:
        break
    if cv.waitKey(1) and 0xFF == ord("e"):
        break
result.release()
cap.release()
cv.destroyAllWindows()
    
