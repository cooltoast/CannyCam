#!/usr/bin/env python2.7

import os

import cv2

from basecam import BaseCam
from util import wait_frames


class HaarCam(BaseCam):
    HAAR_CASCADE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    'xmls',
                                    'haarcascade_frontalface_default.xml')
    face_cascade = cv2.CascadeClassifier(HAAR_CASCADE_PATH)

    def detect_faces(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

        for x, y, w, h in faces:
            cv2.rectangle(img,
                          (x, y),
                          (x + w, y + h),
                          (255, 0, 0),
                          thickness=2)

        return img

    def run(self, frame_throttle):
        """
        Run main HaarCam loop.

        :param frame_throttle: Number of frames to throttle for
        capturing and processing an image from the webcam.
        """
        for _ in wait_frames(throttle=frame_throttle):
            ret_val, img = self.cam.read()
            detected = self.detect_faces(img)

            cv2.imshow(self.window, detected)

            # esc to quit
            if cv2.waitKey(1) == 27:
                break

        cv2.destroyWindow(self.window)


def main():
    h = HaarCam('haarcam')
    h.run(frame_throttle=10)


if __name__ == '__main__':
    main()
