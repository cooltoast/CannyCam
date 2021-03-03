import cv2

from basecam import BaseCam
from util import apply_doc, get_cascade_file_path, is_escape, wait_frames


class HaarCam(BaseCam):
    """
    Webcam that performs Haar Cascade object detection on the video stream.
    """

    @apply_doc(BaseCam.__init__)
    def __init__(self, window):
        super(HaarCam, self).__init__(window)

        self._face_classifier = self._init_classifier("haarcascade_frontalface_default.xml")
        self._fullbody_classifier = self._init_classifier("haarcascade_fullbody.xml")
        self._lowerbody_classifier = self._init_classifier("haarcascade_lowerbody.xml")
        self._upperbody_classifier = self._init_classifier("haarcascade_upperbody.xml")

    def detect_parts(self, img, classifier):
        """
        Detect anatomical parts in ``img`` with Haar Cascade object detection.

        :param img: Image read from webcam.
        :param classifier: Classifier to detect anatomical parts.
        """
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        parts = classifier.detectMultiScale(gray, 1.3, 5)

        for x, y, w, h in parts:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), thickness=2)

        return img

    @apply_doc(BaseCam.run)
    def run(self, frame_throttle, classifier=None):
        """
        :param classifier: Classifier to detect anatomical parts. Defaults \
        to a face classifier if ``None``.
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
        """
        Get a face classifier.
        """
        return self._face_classifier

    @property
    def fullbody_classifier(self):
        """
        Get a full body classifier.
        """
        return self._fullbody_classifier

    @property
    def lowerbody_classifier(self):
        """
        Get a lower body classifier.
        """
        return self._lowerbody_classifier

    @property
    def upperbody_classifier(self):
        """
        Get an upper body classifier.
        """
        return self._upperbody_classifier

    def _init_classifier(self, cascade_file):
        """
        Initialize a Haar Cascade Classifier.

        :param cascade_file: Name of cascade file in the ``xmls`` directory.
        """
        return cv2.CascadeClassifier(get_cascade_file_path(cascade_file))


def main():
    h = HaarCam("haarcam")
    h.run(frame_throttle=10)


if __name__ == "__main__":
    main()
