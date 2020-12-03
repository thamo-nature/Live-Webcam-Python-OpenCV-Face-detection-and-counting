#! /usr/bin/python3

import cv2

import sys

cascPath = sys.argv[1]
facecascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = facecascade.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
        cv2.putText(frame, "Number of people detected: " + str(faces.shape[0]), (0,frame.shape[0] -25), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0,255,0), 1)
   # print("Found {0} faces!".format(len(faces)))
    
    if(len(faces) > 3):
        cv2.putText(frame, ("Crowded Now,Keep Distance"), (0,frame.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,0,0), 1)
        
    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
