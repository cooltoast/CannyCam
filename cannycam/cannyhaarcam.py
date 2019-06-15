#!/usr/bin/env python2.7

import cv2

from cannycam import CannyCam
from haarcam import HaarCam
from util import wait_frames


class CannyHaarCam(CannyCam, HaarCam):
    def run(self, frame_throttle):
        """
        Run main CannyHaarCam loop.

        :param frame_throttle: Number of frames to throttle processing for
        capturing an image from the webcam and performing edge detection.
        """
        for _ in wait_frames(throttle=frame_throttle):
            ret_val, img = self.cam.read()
            edge_detected = self.detect_edges(img)
            detected = self.detect_faces(edge_detected)

            cv2.imshow(self.window, detected)

            # esc to quit
            if cv2.waitKey(1) == 27:
                break

        cv2.destroyWindow(self.window)


def main():
    c = CannyHaarCam('cannyhaarcam')
    c.run(frame_throttle=10)


if __name__ == '__main__':
    main()
