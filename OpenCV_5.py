import cv2
import numpy as np

#----------------------CHAPTER 5------------------

image = cv2.imread("car.jpg")

vertical_image = np.hstack((image, image))
horizontal_image = np.vstack((image, image))

cv2.imshow("Vertical Image", vertical_image)
cv2.imshow("Horizontal Image", horizontal_image)