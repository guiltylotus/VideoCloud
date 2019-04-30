import numpy as np
import cv2
import math
import numpy as np
from CloudDetect import *
from multiprocessing import Process

cap = cv2.VideoCapture("rtsp://192.168.10.103:8554/test")
# cap = cv2.VideoCapture('udpsrc port=5000 caps="application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264, payload=(int)96" ! rtph264depay ! decodebin ! videoconvert ! appsink', cv2.CAP_GSTREAMER)

if (cap.isOpened() == False):
    print('Can not open Camera')

count = 0

while(True):

    # Capture frame-by-frame
    ret, frame = cap.read()

    if (count < 1):
        threshold = Kmean(frame)

    CloudFrame = CloudThreshold(frame, threshold)

    count += 1

    cv2.imshow('frame', CloudFrame)
    # cv2.imshow('frame2', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
