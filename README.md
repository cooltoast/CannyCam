CannyCam
========

Uses webcam stream and performs Canny Edge Detection and Haar Cascade image detection.

Canny Edge Detection removes noise from image, giving black background and white outline. This accentuates sharp edges in the image, making it very easy to detect a target.

Haar Cascade image detection actually detects the target, given a training set of positive images (pictures of the target) and negative images (pictures not containing target, should be images of the physical backgroud used for the experiment).

Together, they take a video as a stream of images, to isolate and detect the target.

Targets used: face, upper body, lower body, hands. Knee, elbow, smaller body parts are work in progress.

Next step is to implement this into a diagnostic image detection program for assisting doctors. E.g. patient goes to doctor with broken ankle, doctor takes x-ray, diagnostic image detection program may be able to detect certain problems with patient's ankle upon scanning the x-ray. 

CannyCam. Better than a nannycam.

Installation
----

Install OpenCV with Python
```
sudo apt-get install python-opencv
```
To run haarcam.py
```
python haarcam.py
```
To run cannycam.py
```
python cannycam.py
```
