import sympy
from sympy import I

def apply_newtons_method(polynomial : sympy.Poly, derivative : sympy.Poly,  initial_guess : float, iterations : int):
    new_guess = initial_guess
    for i in range(iterations):
        step = (polynomial.eval(new_guess) / derivative.eval(new_guess))
        new_guess -= step
    return new_guess


def apply_newtons_method_complex(polynomial : sympy.Poly, derivative : sympy.Poly, initial_guess: tuple, iterations: int):
    """
    :param polynomial: Dictionnary, key is the power, element is the factor
    :param initial_guess: Complex number, first number of the tuple is the real part, second is the imaginary part.
    :param iterations: Number of times to apply newton's method.
    :return: One approximated root (the root returned depends on the initial guess)
    """

    new_guess = initial_guess[0] + initial_guess[1]*I
    for i in range(iterations):
        new_guess -= (polynomial.eval(new_guess) / derivative.eval(new_guess))
    new_guess = new_guess.as_real_imag()
    return (new_guess[0], new_guess[1])
