# Imports necessary packages
import cv2 as cv
import numpy as np

def processImage(image):
    # Creates a mask
    # https://pyimagesearch.com/2021/01/19/image-masking-with-opencv/ Lines 20-26
    roi = np.zeros(image.shape[:2], dtype="uint8")
    cv.rectangle(roi, (500, 500), (900, 900), 255, -1)
    mask = cv.bitwise_and(image, image, mask=roi)

    # Applies gaussian and median blur
    # https://github.com/adityagandhamal/road-lane-detection/blob/master/detection_on_vid.py Lines 35-38
    gray = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    gray_scale = cv.GaussianBlur(gray, (15, 15), 0)
    median_blur = cv.medianBlur(gray_scale, 5)
    canny_image = cv.Canny(median_blur, 100, 50)

    # Creates hough lines around image
    # https://github.com/adityagandhamal/road-lane-detection/blob/master/detection_on_vid.py Line 42
    lines = cv.HoughLinesP(canny_image, 1, np.pi / 180, threshold = 10, minLineLength = 10, maxLineGap = 15)

    #Displays hough lines
    #https://github.com/adityagandhamal/road-lane-detection/blob/master/detection_on_vid.py Line 14-19
    lines_list = []
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv.line(image, (x1, y1), (x2, y2), (0, 255, 0), 10)
            if x2/x1 == y2/y1:
                lines_list.append([(x1, y1), (x2, y2)])
                print(lines_list)

