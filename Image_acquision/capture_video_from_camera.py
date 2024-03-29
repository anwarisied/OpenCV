"""
//Capture Video from Camera 
Tested on:
Python3 on Ubuntu 22.03
19/07/2022
Source: https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
"""
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    
    cv2.imshow('frame', gray)
    #Replace with cv2.imshow('frame', gray) for RGB instead of Gray
    if cv2.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()