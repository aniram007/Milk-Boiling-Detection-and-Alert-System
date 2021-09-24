import numpy as np
import cv2
import time
font=cv2.FONT_HERSHEY_SIMPLEX

cap=cv2.VideoCapture("Milk.mp4")
ret,frame=cap.read()
rows,cols=frame.shape[:2]
filename = 'Output2.avi'
codec = cv2.VideoWriter_fourcc('F', 'M', 'P', '4')
framerate = 30
resolution = (cols,rows)
VideoFileOutput = cv2.VideoWriter(filename, codec, framerate, resolution)
start=time.time()
starting=True
frame_count=0
state = 0
areas = []
while True:
    if starting:
        start=time.time()
        starting=False
    ret,frame=cap.read()
    if not ret:
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret,thresh=cv2.threshold(gray,190,255,cv2.THRESH_BINARY)
    mblur=cv2.medianBlur(thresh,11)
    contours,hierarchy=cv2.findContours(mblur,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    c=max(contours,key=cv2.contourArea)
    M = cv2.moments(c)
    x,y = int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"])
    
    #cv2.drawContours(frame,[c],0,(255,0,0),3)
    area=cv2.contourArea(c)
    areas.append(area)
    if len(areas) >=10:
        area = np.array(areas[-10:]).sum()/10
    if(area<24250):
        if state == 0:
            cv2.putText(frame,'BOILING',(frame.shape[1]-140,frame.shape[0]-20), font, 1, (0,255,0), 3)
            color_tuple = (0,255,0)
        else:
            cv2.putText(frame,'COOLED',(frame.shape[1]-140,frame.shape[0]-20), font, 1, (255,0,0), 3)
            color_tuple = (255,0,0)
    elif(area>=24250 and area<=25750):
        if state == 0 :
            state = 1
        if state == 2:
            state = 3
        if state == 1:
            cv2.putText(frame,'GET READY',(frame.shape[1]-180,frame.shape[0]-20), font, 1, (0,255,255), 3)
            color_tuple = (0,255,255)
        if state == 3:
            cv2.putText(frame,'COOLING',(frame.shape[1]-180,frame.shape[0]-20), font, 1, (255,255,0), 3)
            color_tuple = (255,255,0)
    else:
        if state == 1:
            state=2
        if state == 2:
            cv2.putText(frame,'TURN OFF STOVE!',(frame.shape[1]-300,frame.shape[0]-20), font, 1, (0,0,255), 3)
            color_tuple = (0,0,255)
        else:
            cv2.putText(frame,'COOLING',(frame.shape[1]-180,frame.shape[0]-20), font, 1, (255,255,0), 3)
            color_tuple = (255,255,0)
        
    
    frame_count+=1
    cv2.rectangle(frame,(x-90,y-90),(x+100,y+80),color_tuple,2)
##    print(len(contours))   
    cv2.imshow("Frame",frame)
    VideoFileOutput.write(frame)
    cv2.imshow("Mask",mblur)
    if cv2.waitKey(3)==27:
        break
ending=time.time()
fps = frame_count/(ending-start)
print("FPS:",fps)
cap.release()
VideoFileOutput.release()
cv2.destroyAllWindows()
