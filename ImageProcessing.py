#Imports necessary packages
import cv2 as cv
import numpy as np

def processImage(image):
    # Applies gaussian and median blur
    #https://github.com/adityagandhamal/road-lane-detection/blob/master/detection_on_vid.py Lines 35-38
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray_scale = cv.GaussianBlur(gray, (15, 15), 0)
    median_blur = cv.medianBlur(gray_scale, 5)
    canny_image = cv.Canny(median_blur, 130, 220)

    # Creates hough lines around image
    #https://github.com/adityagandhamal/road-lane-detection/blob/master/detection_on_vid.py Line 42
    lines = cv.HoughLinesP(canny_image, 1, np.pi / 180, threshold=10, minLineLength=15, maxLineGap=2)


