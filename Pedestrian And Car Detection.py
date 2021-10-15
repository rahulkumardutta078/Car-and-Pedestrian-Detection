# Importing Libraries

import cv2

# Loading Cascade

car_cascade=cv2.CascadeClassifier('haar-cascade-files-master\car.xml')
pedestrian_cascade=cv2.CascadeClassifier('haar-cascade-files-master\haarcascade_fullbody.xml')


# Working Function

def detect(gray,frame):
    car=car_cascade.detectMultiScale(gray,1.4,2)
    for (x,y,w,h) in car:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        
    
    pedestrian=pedestrian_cascade.detectMultiScale(frame,1.2,3)
    for (ex,ey,ew,eh) in pedestrian:
        cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
    return frame

# Initiate video capture for video file

cap=cv2.VideoCapture('videoplayback.mp4')
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canvas=detect(gray,frame)
    
    cv2.imshow('Video',canvas)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
