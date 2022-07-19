"""
Henry Gardner
Rear-view Camera for any car

Parts Needed:
    - Raspberry Pi (3+)
    - Screen (I picked a 7 inch display)
    - GPS usb locator
    - USB Camera

This file contains the neccesary components for a basic camera output.    
"""

import numpy
import cv2

# connect to the usb camera
video = cv2.VideoCapture(0)

while(True):
    # capture frame by frame (from cv2 docs)
    ret, frame = video.read()

    # display frame
    cv2.imshow('Camera', frame)

    # sleep for a second to verify not terminating
    if cv2.waitKey(1) == ord('q'):
        break

# destroy windows and video when complete
video.release()
cv2.destroyAllWindows()
