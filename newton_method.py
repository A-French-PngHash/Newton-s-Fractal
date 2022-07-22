import operations
import polynomials
from numpy.polynomial import Polynomial
import numpy


def apply_newtons_method(polynomial : dict, derivative : dict,  initial_guess : float, iterations : int):
    new_guess = initial_guess
    for i in range(iterations):
        step = - (polynomials.calculate_image(polynomial, new_guess) / polynomials.calculate_image(derivative, new_guess))
        new_guess += step
    return new_guess


def apply_newtons_method_complex(polynomial : Polynomial, derivative : Polynomial, initial_guess: list, iterations: int):
    """
    :param polynomial: Dictionnary, key is the power, element is the factor
    :param initial_guess: Complex number, first number of the tuple is the real part, second is the imaginary part.
    :param iterations: Number of times to apply newton's method.
    :return: One approximated root (the root returned depends on the initial guess)
    """

    new_guess =  complex(initial_guess[0], initial_guess[1])
    for i in range(iterations):
        new_guess -= polynomial(new_guess) / derivative(new_guess)
    return new_guess
