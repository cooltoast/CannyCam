import abc

import cv2


class BaseCam(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, window):
        """
        :param window: Name of the window that BaseCam will open.
        """
        self.window = window
        self.cam = cv2.VideoCapture(0)

        cv2.namedWindow(window)

    @abc.abstractmethod
    def run(self, frame_throttle):
        """
        Run main BaseCam loop.

        :param frame_throttle: Number of frames to throttle for
        capturing and processing an image from the webcam.
        """
        raise NotImplementedError()
