# Imports necessary packages
import cv2 as cv
import numpy as np
import matplotlib as lib

def processImage(image):
    # Applies gaussian blur, median blur, and canny on the image
    # https://github.com/adityagandhamal/road-lane-detection/blob/master/detection_on_vid.py Lines 35-38
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray_scale = cv.GaussianBlur(gray, (15, 15), 0)
    median_blur = cv.medianBlur(gray_scale, 5)
    canny_image = cv.Canny(median_blur, 100, 20)

    # Creates a mask around desired area
    # https://pyimagesearch.com/2021/01/19/image-masking-with-opencv/ Lines 20-26
    roi = np.zeros(image.shape[:2], dtype="uint8")
    cv.rectangle(roi, (50, 50), (400, 400), 1, -1)
    mask = cv.bitwise_and(canny_image, canny_image, mask=roi)
    #Displays the mask
    cv.rectangle(image, (50, 50), (400, 400), (255, 0, 0), 5)

    # Creates hough lines around image
    # https://github.com/adityagandhamal/road-lane-detection/blob/master/detection_on_vid.py Line 42
    lines = cv.HoughLinesP(mask, 1, np.pi / 180, threshold = 10, minLineLength = 10, maxLineGap = 15)

    #Displays hough lines
    #https://github.com/adityagandhamal/road-lane-detection/blob/master/detection_on_vid.py Line 14-19

    #Prevents program from crashing if no lines detected
    if lines is not None:
        for line in lines:
            #Creates lines
            x1, y1, x2, y2 = line[0]
            line_arr = []
            line_arr.append(line)
            print(line_arr[0])
            line_arr.append(line_arr)

            #Displays parallel lines
            cv.line(image, (x1, y1), (x2, y2), (0, 255, 0), 10)
            # https://www.geeksforgeeks.org/program-find-slope-line/ Line 4
            #Calculates slope
            slope = (y2 - y1) / (x2 - x1)
            print(slope)


        #Calculates centerline
        if slope > 1:
            cv.line(image, (190, 218), (335, 290), (0, 0, 255), 10)
        elif slope < 1:
            cv.line(image, (250, 218), (200, 372), (0, 0, 255), 10)
