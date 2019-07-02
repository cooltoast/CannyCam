import os


ESCAPE_ASCII = 27
XML_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'xmls')


def get_cascade_file_path(cascade_file):
    """
    Formats a full filepath to the XML ``cascade_file`` in the ``xmls`` directory.

    :param cascade_file: XML file.
    """
    return os.path.join(XML_DIRECTORY, cascade_file)


def inherit_doc(parent):
    """
    Decorator that will prepend ``parent``'s docstring to the decorated function.

    :param parent: Function whose docstring should be used to prepend with.
    """
    def decorator(func):
        parent_doc = parent.__doc__

        if func.__doc__ is None:
            func.__doc__ = parent_doc
        else:
            func.__doc__ = '\n'.join((parent_doc, func.__doc__))

        return func

    return decorator


def is_escape(key):
    """
    Determines if ``key`` is the ESC key.

    :param key: Key to check.
    """
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
