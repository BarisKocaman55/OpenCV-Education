import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#--------------------------CHAPTER 1--------------------
#Reading Images
#image = cv2.imread("car.jpg")
#image = cv2.resize(image, (480,300))
#cv2.imshow("Car Image", image)
#cv2.waitKey(0)

#Video Captureq
#video = cv2.VideoCapture("testVideo.mp4")
#
#while True:
#    success, img = video.read()
#    cv2.imshow("Video", img)
#    if cv2.waitKey(1) & 0xFF==ord("q"):
#        break
    
#WebCam Capture
video = cv2.VideoCapture(0)
video.set(3,640) #width
video.set(4,480) #height

while True:
    success, img = video.read()
    cv2.imshow("Video", img)
    
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break