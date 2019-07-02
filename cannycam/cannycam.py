#!/usr/bin/env python2.7

import cv2

from basecam import BaseCam
from util import inherit_doc, is_escape, wait_frames


class CannyCam(BaseCam):
    """
    Webcam that performs Canny Edge Detection on the video stream.
    """
    KERNEL_SIZE = 3
    MIN_THRESHOLD = 0
    MAX_THRESHOLD = 100
    RATIO = 3

    @inherit_doc(BaseCam.__init__)
    def __init__(self, window):
        super(CannyCam, self).__init__(window)
        self.threshold = self.MIN_THRESHOLD

        cv2.createTrackbar('Threshold',
                           self.window,
                           self.threshold,
                           self.MAX_THRESHOLD,
                           self._on_threshold_change)

    def detect_edges(self, img, color=True):
        """
        :param img: Image read from webcam.
        :param color: Boolean to indicate if should use color. Defaults to True.
        """
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        detected_edges = cv2.GaussianBlur(gray, (3, 3), 0)
        detected_edges = cv2.Canny(detected_edges,
                                   self.threshold,
                                   self.threshold * self.RATIO,
                                   apertureSize=self.KERNEL_SIZE)

        # add colors to edges from original image
        return cv2.bitwise_and(img, img, mask=detected_edges) if color else detected_edges

    @inherit_doc(BaseCam.run)
    def run(self, frame_throttle):
        try:
            for _ in wait_frames(throttle=frame_throttle):
                ret_val, img = self.cam.read()
                detected = self.detect_edges(img)

                cv2.imshow(self.window, detected)

                # esc to quit
                if is_escape(cv2.waitKey(1)):
                    break
        finally:
            cv2.destroyWindow(self.window)

    def _on_threshold_change(self, threshold):
        self.threshold = threshold


def main():
    c = CannyCam('cannycam')
    c.run(frame_throttle=10)


if __name__ == '__main__':
    main()
