import cv2
import numpy as np
import pandas as pd

#----------------------CHAPTER 2-----------------------
image = cv2.imread("car.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur_image = cv2.GaussianBlur(gray_image, (7,7), 0)

kernel = np.ones((3,3), np.uint8)

imgCanny = cv2.Canny(gray_image, 100, 100)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgCanny, kernel, iterations=1)

cv2.imshow("Normal Image", image)
cv2.imshow("Gray Image", gray_image)
cv2.imshow("Blured Image", blur_image)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDilation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)