#!/usr/bin/env python2.7

import cv2

from basecam import BaseCam
from util import get_cascade_file_path, is_escape, wait_frames


class HaarCam(BaseCam):
    def __init__(self, window):
        """
        :param window: Name of the window that BaseCam will open.
        """
        super(HaarCam, self).__init__(window)

        self._face_classifier = self._init_classifier('haarcascade_frontalface_default.xml')
        self._fullbody_classifier = self._init_classifier('haarcascade_fullbody.xml')
        self._lowerbody_classifier = self._init_classifier('haarcascade_lowerbody.xml')
        self._upperbody_classifier = self._init_classifier('haarcascade_upperbody.xml')

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

        try:
            for _ in wait_frames(throttle=frame_throttle):
                ret_val, img = self.cam.read()
                detected = self.detect_parts(img, classifier)

                cv2.imshow(self.window, detected)

                # esc to quit
                if is_escape(cv2.waitKey(1)):
                    break
        finally:
            cv2.destroyWindow(self.window)

    @property
    def face_classifier(self):
        return self._face_classifier

    @property
    def fullbody_classifier(self):
        return self._fullbody_classifier

    @property
    def lowerbody_classifier(self):
        return self._lowerbody_classifier

    @property
    def upperbody_classifier(self):
        return self._upperbody_classifier

    def _init_classifier(self, cascade_file):
        """
        Initialize a Haar Cascade Classifier.

        :param cascade_file: Name of cascade file in the ``xmls`` directory.
        """
        return cv2.CascadeClassifier(get_cascade_file_path(cascade_file))


def main():
    h = HaarCam('haarcam')
    h.run(frame_throttle=10)


if __name__ == '__main__':
    main()
