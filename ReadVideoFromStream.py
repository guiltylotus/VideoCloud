import numpy as np
import cv2
import math

# Capture Video and set resolution
# print(cv2.getBuildInformation())
# cap = cv2.VideoCapture("videotestsrc ! appsink")
# cap = cv2.VideoCapture('udpsrc port=5000 caps="application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264, payload=(int)96" ! rtph264depay ! decodebin ! videoconvert ! appsink', cv2.CAP_GSTREAMER)
# cap = cv2.VideoCapture("tcp://192.168.10.103:5000")
cap = cv2.VideoCapture("rtsp://192.168.10.103:8554/test")
# cap = cv2.VideoCapture('udpsrc uri="udp://192.168.10.103:5000" caps="application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264, payload=(int)96" ! rtph264depay ! decodebin ! videoconvert ! appsink', cv2.CAP_GSTREAMER)
# cap = cv2.VideoCapture('autovideosrc ! videoconvert ! appsink')

if (cap.isOpened() == False):
    print('failed')

while(True):

    # Capture frame-by-frame
    ret, frame = cap.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)
    #cv2.imshow('frame2', frame2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
