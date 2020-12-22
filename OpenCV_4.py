import numpy as np
import pandas as pd
import cv2

#----------------CHAPTER4----------------

image = np.zeros((512,512,3), np.uint8)
image[200:300,100:300] = 255,0,0

#cv2.imshow("Image", image)
#print(image.shape)

#Drawing line, rectange, circle
black_image = np.zeros((512,512,3), np.uint8)
cv2.line(black_image, (0,0), (black_image.shape[1], black_image.shape[0]), (0,255,0), 3)
cv2.rectangle(black_image, (0,0), (100,100), (0,0,255), 3)
cv2.circle(black_image, (400,50), 30, (255,0,0), 3)
cv2.imshow("Line", black_image)

cv2.waitKey(0)