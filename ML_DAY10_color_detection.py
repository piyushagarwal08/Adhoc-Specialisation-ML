#!/usr/bin/python3
import cv2
cap = cv2.VideoCapture(0)
i = 10
while True:
    status,frame = cap.read()
    # detecting red color 
    redimg =  cv2.inRange(frame,(0,0,0),(i,i,255))
    cv2.imshow('redcolor',redimg)
    cv2.imshow('liverfcolor',frame)
    i = i+1
    if cv2.waitKey(10) & 0xff == ord('q'):
      break
cv2.destroyAllWindows()
cap.release()

