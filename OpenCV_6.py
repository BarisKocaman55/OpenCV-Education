import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

def read_image(path):
    image = cv2.imread(path)
    return image


def show_image(name, image):
    cv2.imshow(name, image)
    

def cvt2Gray(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image
    
def cvt2HSV(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return hsv_image
    

def empty():
    pass


if __name__ == "__main__":
    path = "car.jpg"
    cv2.namedWindow("TrackBars")
    cv2.resizeWindow("TrackBars", 640, 300)
    cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
    cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
    cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
    cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
    cv2.createTrackbar("Value Min", "TrackBars", 0, 255, empty)
    cv2.createTrackbar("Value Max", "TrackBars", 255, 255, empty)
    
    
    while True:
        image = read_image(path)
        show_image("Original Image", image)
        hue_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
        hue_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
        sat_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
        sat_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
        value_min = cv2.getTrackbarPos("Value Min", "TrackBars")
        value_max = cv2.getTrackbarPos("Value Max", "TrackBars")
        
        
        
        value_list = np.array([hue_min, hue_max, sat_min, sat_max, value_min, value_max])
        print(value_list)
        
        
        hsv_image = cvt2HSV(image)
        lower = np.array([hue_min, sat_min, value_min])
        upper = np.array([hue_max, sat_max, value_max])
        mask = cv2.inRange(hsv_image, lower, upper)
        imResult = cv2.bitwise_and(image, image, mask=mask)

        show_image("HSV Image", hsv_image)
        show_image("Mask Image", mask)
        cv2.waitKey(1)