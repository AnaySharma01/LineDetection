#Imports necessary packages
import cv2 as cv

#Imports necessary function
import ImageDisplaying
import ImageReading

#Loads the image
file = cv.VideoCapture(0)
ImageReading.readImage()

#Applies image detection

#Displays image with hough lines
ImageDisplaying.displayImage()
