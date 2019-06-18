import os


ESCAPE_ASCII = 27
XML_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'xmls')


def get_cascade_file_path(cascade_file):
    return os.path.join(XML_DIRECTORY, cascade_file)


def is_escape(key):
    return key == ESCAPE_ASCII


def wait_frames(throttle):
    """
    Returns a generator that yields every ``throttle`` frames.

    :param throttle: Number of frames to wait before yielding.
    """
    i = 0

    while True:
        if i == throttle:
            i = 0
            yield

        i += 1
