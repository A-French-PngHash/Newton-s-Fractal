import cmath
import math
import numpy

"""
I just wasn't feeling like implementing divisions manually xD
Maybe later :p
"""

def divide(complex_1 : tuple, complex_2 : tuple) -> tuple:
    output = (complex(complex_1[0], complex_1[1]) / complex(complex_2[0], complex_2[1]))
    return (output.real, output.imag)

def distance_between_points(first : tuple, second : tuple):
    """
    Give the distance between two point.
    :param first:
    :param second:
    :return:
    """
    distance = math.sqrt((first[0] - second[0])**2 + (first[1] - second[1])**2)
    return distance
