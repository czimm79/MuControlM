import numpy as np
import pyqtgraph as pg
from PyQt5.QtCore import QEventLoop, QTimer


def xy_to_cylindrical(x, y):
    """
    Convert the x and y coordinates from the joystick into degrees from 0 to 360.
    Args:
        x: x coordinate from joystick
        y: y coordinate from joystick

    Returns:
        magnitude: magnitude of x,y vector
        degrees: degrees from 0-360 starting from the positive y axis, clockwise
    """

    magnitude = np.around(np.linalg.norm((x, y)), 2)
    degrees = np.degrees(np.arctan2(x, y))
    degrees = degrees % 360  # Modulo division accounts for negative degree values pi to 2pi.
    degrees = np.around(degrees, 0)  # Round to the nearest integer
    return magnitude, degrees


def set_style():
    """ Simply set some config options and themes. """
    pg.setConfigOption('background', 'w')
    pg.setConfigOption('foreground', 'k')
    pg.setConfigOptions(antialias=True)


def qtsleep(t):
    """Sleep the current thread for `t` seconds. Non-blocking, so does not freeze the program like normal python sleep() would.

    Args:
        t (float): time in s to sleep 
    """
    loop = QEventLoop()
    QTimer.singleShot(t * 1000, loop.quit)
    loop.exec_()


def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)