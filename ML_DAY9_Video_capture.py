#!/usr/bin/python3

import cv2

# starting camera
capture = cv2.VideoCapture(0)

while capture.isOpened():
    status,frame = capture.read()

    # to show 2 different screens at real time 


    print(frame.shape)
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    #cv2.imshow('capture1',grey)

    # to draw line
    cv2.line(frame,(0,300),(300,300),(0,255,0),4)

    # to draw rectangle
    cv2.rectangle(frame,(50,50),(400,300),(0,0,255),3)

    # to draw circle
    cv2.circle(frame,(500,400),100,(100,120,200),4)
    
    # to write text
    font = cv2.FONT_HERSHEY_SIMPLEX         # this is style of font to be used
    # putText(image-name,what-to-type,where-to-type,font,width of font,color,length-of-alphabhet,straight-line)
    cv2.putText(frame,'PYKID',(100,360),font,3,(0,2,55),3,cv2.LINE_AA)

    cv2.imshow('capture',frame)
   # if cv2.waitKey(10) & 0xff == ord('q'):
    if cv2.waitKey(4) == 13:    # 13: stands for enter key      # 1 second is the differentiate factor for human eye that is 25 img in 1 sec
        break                     # to hold the camera

#cv2.destroyAllWindows() # to delete single window cv2.destroyWindow('window-name')
capture.release()
