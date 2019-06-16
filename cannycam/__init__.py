from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from .cannycam import CannyCam
from .cannyhaarcam import CannyHaarCam
from .haarcam import HaarCam
