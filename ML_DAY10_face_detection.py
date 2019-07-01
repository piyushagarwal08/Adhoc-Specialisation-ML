#!/user/bin/python3

import cv2

# calling classifier
clf = cv2.CascadeClassifier('face.xml')

# loading face data
capture = cv2.VideoCapture(0)

while capture.isOpened():
    status,frame = capture.read()

    # Now we can apply classifier in live frame
    face = clf.detectMultiScale(frame,1.5,5)  # classifier tuning data
   # cv2.imshow('face',face)

    print(face) # prints initial coordinate(x,y) and height and weight
    for x,y,h,w in face:
        cv2.rectangle(frame,(x,y),(x+h,y+w),(0,0,255),3)
        # only face
        facedata = frame[x:x+h,y:y+w]
        cv2.imshow('face',facedata)
    cv2.imshow('face1',frame)
    if cv2.waitKey(10) == 13:
        break

cv2.destroyAllWindows()
capture.release()


