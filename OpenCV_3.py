import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

##-------------------CHAPTER 3--------------------
def read_image(path):
    image = cv2.imread(path)
    return image

def show_image(image):
    cv2.imshow("", image)
    
def resize_image(image, height, width):
    image = cv2.resize(image, (height, width))
    return image
    
if __name__ == "__main__":
    path = "car.jpg"
    image = read_image(path)
    image = cv2.resize(image, (480, 300))
    print(image.shape)
    show_image(image)