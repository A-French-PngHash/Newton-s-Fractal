import cmath
import math


def distance_between_points(first : tuple, second : tuple):
    """
    Give the distance between two point.
    :param first:
    :param second:
    :return:
    """
    distance = math.sqrt((first[0] - second[0])**2 + (first[1] - second[1])**2)
    return distance
