#!/usr/bin/env python

import cv

HAAR_CASCADE_PATH = "/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
CAMERA_INDEX = 0
storage = cv.CreateMemStorage()
cascade = cv.Load(HAAR_CASCADE_PATH)

def detect_faces(image):
    faces = []
    detected = cv.HaarDetectObjects(image, cascade, storage, 1.2, 2, cv.CV_HAAR_DO_CANNY_PRUNING, (100,100))
    if detected:
        #print detected
        for (x,y,w,h),n in detected:
            faces.append((x,y,w,h))
    return faces

if __name__ == "__main__":
    cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
    capture = cv.CaptureFromCAM(CAMERA_INDEX)
    faces = []

    i = 0
    while True:
        image = cv.QueryFrame(capture)

        # Only run the Detection algorithm every 5 frames to improve performance
        if i%5==0:
            faces = detect_faces(image)
            print faces

        for (x,y,w,h) in faces:
            cv.Rectangle(image, (x,y), (x+w,y+h), 255)

        cv.ShowImage("w1", image)
        c=cv.WaitKey(10)
        if c==27:
            exit()
        i += 1