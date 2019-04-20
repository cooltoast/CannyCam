def wait_frames(throttle):
    """
    Returns a generator that yields every ``throttle`` frames.

    :param throttle: Number of frames to wait before yielding.
    """
    i = 0
    while True:
        if i % throttle == 0:
            yield i

        i += 1
