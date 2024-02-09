#Imports necessary packages
import cv2 as cv

#Imports function for reading images
import ImageProcessing
import ImageDisplaying

def readImage():
    #Variable needed for displaying the video
    #https://geeksforgeeks.org/python-play-a-video-using-opencv/ lines 15 - 20
    videoIsPlaying = True

    #Starts the video capture
    video = cv.VideoCapture(0)
    
    #While the video is playing, read the frame, process it & display it
    while videoIsPlaying == True:
        videoIsPlaying, frame = video.read()
        ImageProcessing.processImage(frame)
        ImageDisplaying.displayImage(frame)
    cv.destroyAllWindows()

