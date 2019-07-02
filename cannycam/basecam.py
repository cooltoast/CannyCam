import abc

import cv2


class BaseCam(object):
    """
    Abstract class for running a cv2 webcam.
    """

    __metaclass__ = abc.ABCMeta

    def __init__(self, window):
        """
        :param window: Name of the window that the cv2 webcam will open.
        """
        self.window = window
        self.cam = cv2.VideoCapture(0)

        cv2.namedWindow(window)

    @abc.abstractmethod
    def run(self, frame_throttle):
        """
        Run main cv2 webcam capture loop.

        :param frame_throttle: Number of frames to throttle for \
        capturing and processing an image from the webcam.
        """
        raise NotImplementedError()
