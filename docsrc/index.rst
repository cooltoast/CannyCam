.. CannyCam documentation master file, created by
   sphinx-quickstart on Mon Jul  1 16:31:53 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

CannyCam
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Description
-------------------
Uses webcam stream and performs Canny Edge Detection and Haar Cascade image detection.

Canny Edge Detection removes noise from image, giving black background and white outline. This accentuates sharp edges in the image, making it very easy to detect a target.

Haar Cascade image detection actually detects the target, given a training set of positive images (pictures of the target) and negative images (pictures not containing target, should be images of the physical backgroud used for the experiment).

Together, they take a video as a stream of images, to isolate and detect the target.

Targets used: face, upper body, lower body, hands. Knee, elbow, smaller body parts are work in progress.

Next step is to implement this into a diagnostic image detection program for assisting doctors. E.g. patient goes to doctor with broken ankle, doctor takes x-ray, diagnostic image detection program may be able to detect certain problems with patient's ankle upon scanning the x-ray.

CannyCam. Better than a nannycam.

Installation
-------------------
.. code-block:: bash

  pip install cannycam

Run
-------------------
From the command line

.. code-block:: bash

  python -m cannycam.cannycam
  python -m cannycam.haarcam
  python -m cannycam.cannyhaarcam

Or in python

.. code-block:: python

  import cannycam

  cannycam.cannycam.main()
  cannycam.haarcam.main()
  cannycam.cannyhaarcam.main()


API
-------------------
Webcams
^^^^^^^^^^^^^^^^^^^
.. automodule:: cannycam.basecam
   :inherited-members:
   :members:

.. automodule:: cannycam.cannycam
   :show-inheritance:
   :inherited-members:
   :members:

.. automodule:: cannycam.haarcam
   :show-inheritance:
   :inherited-members:
   :members:
   :exclude-members: _init_classifier

.. automodule:: cannycam.cannyhaarcam
   :show-inheritance:
   :inherited-members:
   :members:

Utils
^^^^^^^^^^^^^^^^^^^
.. automodule:: cannycam.util
   :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
