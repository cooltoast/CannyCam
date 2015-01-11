import cv
import cv2
import numpy as np
from haarcam import detect_faces

cv2.namedWindow("canny cam")
capture = cv.CaptureFromCAM(0)
lowThreshold = 0
max_lowThreshold = 100
ratio = 3
kernel_size = 3


def repeat():
    frame = cv.QueryFrame(capture)
    
    # Only run the Detection algorithm every 5 frames to improve performance
    if i%5==0:
        faces = detect_faces(frame)
        print faces

    for (x,y,w,h) in faces:
        cv.Rectangle(frame, (x,y), (x+w,y+h), 255)

    img = np.asarray(frame[:,:])

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    detected_edges = cv2.GaussianBlur(gray,(3,3),0)
    detected_edges = cv2.Canny(detected_edges,lowThreshold,lowThreshold*ratio,apertureSize = kernel_size)
    dst = cv2.bitwise_and(img,img,mask = detected_edges)  # just add some colours to edges from original image.
    
    cv2.imshow('canny cam',detected_edges)

    c = cv.WaitKey(10)
    if c == 27:
        exit()


def SetThreshold(slider_value):
    global lowThreshold
    lowThreshold = slider_value
    

if __name__ == '__main__':
  cv2.createTrackbar('Min threshold','canny cam',lowThreshold, max_lowThreshold, SetThreshold)

  i = 0
  while True:
      repeat()

