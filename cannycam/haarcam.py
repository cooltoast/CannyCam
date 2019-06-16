#!/usr/bin/env python2.7

import os

import cv2

from basecam import BaseCam
from util import wait_frames


XML_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'xmls')


class HaarCam(BaseCam):
    def __init__(self, window):
        """
        :param window: Name of the window that BaseCam will open.
        """
        super(HaarCam, self).__init__(window)

        self.face_classifier = self._init_classifier('haarcascade_frontalface_default.xml')
        self.fullbody_classifier = self._init_classifier('haarcascade_fullbody.xml')
        self.lowerbody_classifier = self._init_classifier('haarcascade_lowerbody.xml')
        self.upperbody_classifier = self._init_classifier('haarcascade_upperbody.xml')

    def detect_parts(self, img, classifier):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        parts = classifier.detectMultiScale(gray, 1.3, 5)

        for x, y, w, h in parts:
            cv2.rectangle(img,
                          (x, y),
                          (x + w, y + h),
                          (255, 0, 0),
                          thickness=2)

        return img

    def run(self, frame_throttle, classifier=None):
        """
        Run main HaarCam loop.

        :param frame_throttle: Number of frames to throttle for capturing
        and processing an image from the webcam.
        :param classifier: Classifier to detect anatomical parts. Defaults
        to a face classifier.
        """
        if classifier is None:
            classifier = self.face_classifier

        for _ in wait_frames(throttle=frame_throttle):
            ret_val, img = self.cam.read()
            detected = self.detect_parts(img, classifier)

            cv2.imshow(self.window, detected)

            # esc to quit
            if cv2.waitKey(1) == 27:
                break

        cv2.destroyWindow(self.window)

    def _init_classifier(self, cascade_file):
        """
        Initialize a Haar Cascade Classifier.

        :param cascade_file: Name of cascade file in the ``xmls`` directory.
        """
        cascade_path = os.path.join(XML_DIRECTORY, cascade_file)

        return cv2.CascadeClassifier(cascade_path)


def main():
    h = HaarCam('haarcam')
    h.run(frame_throttle=10)


if __name__ == '__main__':
    main()
