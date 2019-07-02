import os


ESCAPE_ASCII = 27
XML_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'xmls')


def apply_doc(source):
    """
    Decorator that will prepend ``source``'s docstring to the decorated \
    object's docstring.

    :param source: Object with docstring to be prepended onto the decorated object.
    """
    def decorator(target):
        source_doc = source.__doc__

        if target.__doc__ is None:
            target.__doc__ = source_doc
        else:
            target.__doc__ = '\n'.join((source_doc, target.__doc__))

        return target

    return decorator


def get_cascade_file_path(cascade_file):
    """
    Formats a full filepath to the XML ``cascade_file`` in the ``xmls`` directory.

    :param cascade_file: XML file.
    """
    return os.path.join(XML_DIRECTORY, cascade_file)


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
