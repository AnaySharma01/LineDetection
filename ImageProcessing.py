# Imports necessary packages
import cv2 as cv
import numpy as np
def processImage(image):
    # Applies gaussian blur, median blur, and canny on the image
    # https://github.com/adityagandhamal/road-lane-detection/blob/master/detection_on_vid.py Lines 35-38
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray_scale = cv.GaussianBlur(gray, (15, 15), 0)
    median_blur = cv.medianBlur(gray_scale, 5)
    canny_image = cv.Canny(median_blur, 100, 20)
    
    # Creates a mask
    # https://pyimagesearch.com/2021/01/19/image-masking-with-opencv/ Lines 20-26
    roi = np.zeros(image.shape[:2], dtype="uint8")
    cv.rectangle(roi, (500, 500), (850, 850), 1, -1)
    mask = cv.bitwise_and(canny_image, canny_image, mask=roi)

    # Creates hough lines around image
    # https://github.com/adityagandhamal/road-lane-detection/blob/master/detection_on_vid.py Line 42
    lines = cv.HoughLinesP(mask, 1, np.pi / 180, threshold = 10, minLineLength = 10, maxLineGap = 15)

    #Displays hough lines
    #https://github.com/adityagandhamal/road-lane-detection/blob/master/detection_on_vid.py Line 14-19

    #Prevents program from crashing if no lines detected
    if lines is not None:
        for line in lines:
            #Creates lines
            x11, y11, x21, y21 = line[0]
            cv.line(image, (x11, y11), (x21, y21), (0, 255, 0), 10)


