import cv2

from cannycam import CannyCam
from haarcam import HaarCam
from util import apply_doc, is_escape, wait_frames


class CannyHaarCam(CannyCam, HaarCam):
    """
    Webcam that performs Canny Edge detection and then \
    Haar Cascade object detection on the video stream.
    """

    @apply_doc(HaarCam.run)
    def run(self, frame_throttle, classifier=None):
        if classifier is None:
            classifier = self.face_classifier

        try:
            for _ in wait_frames(throttle=frame_throttle):
                ret_val, img = self.cam.read()
                edge_detected = self.detect_edges(img)
                detected = self.detect_parts(edge_detected, classifier)

                cv2.imshow(self.window, detected)

                # esc to quit
                if is_escape(cv2.waitKey(1)):
                    break
        finally:
            cv2.destroyWindow(self.window)


def main():
    c = CannyHaarCam("cannyhaarcam")
    c.run(frame_throttle=10)


if __name__ == "__main__":
    main()
