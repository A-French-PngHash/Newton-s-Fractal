import operations
import polynomials
from numpy.polynomial import Polynomial



def apply_newtons_method(polynomial : dict, derivative : dict,  initial_guess : float, iterations : float):
    new_guess = initial_guess
    for i in range(iterations):
        step = - (polynomials.calculate_image(polynomial, new_guess) / polynomials.calculate_image(derivative, new_guess))
        new_guess += step
    return new_guess

def num_apply_newtons_method(polynomial : Polynomial, derivative : Polynomial,  initial_guess : float, iterations : int):
    new_guess = initial_guess
    for i in range(iterations):
        new_guess -= polynomial(new_guess) / derivative(new_guess)
    return new_guess

def apply_newtons_method_complex(polynomial : dict, derivative : dict, initial_guess: list, iterations: int):
    """
    :param polynomial: Dictionnary, key is the power, element is the factor
    :param initial_guess: Complex number, first number of the tuple is the real part, second is the imaginary part.
    :param iterations: Number of times to apply newton's method.
    :return: One approximated root (the root returned depends on the initial guess)
    """

    new_guess = initial_guess
    for i in range(iterations):
        step = operations.divide(
            polynomials.calculate_image_complex(polynomial, new_guess[0], new_guess[1]),
            polynomials.calculate_image_complex(derivative, new_guess[0], new_guess[1])
        )
        new_guess[0] -= step[0]
        new_guess[1] -= step[1]
    return new_guess


def num_apply_newtons_method_complex(polynomial : Polynomial, derivative : Polynomial, initial_guess: complex, iterations: int):
    """
    :param polynomial: Dictionnary, key is the power, element is the factor
    :param initial_guess: Complex number, first number of the tuple is the real part, second is the imaginary part.
    :param iterations: Number of times to apply newton's method.
    :return: One approximated root (the root returned depends on the initial guess)
    """

    new_guess =  initial_guess
    for i in range(iterations):
        new_guess -= polynomial(new_guess) / derivative(new_guess)
    return new_guess


pol = {5: 1, 4 : -0.5, 2: 1, 1: -1, 0: 1}
deriv = polynomials.derivate_polynomial(pol)
guess = [1.3, 2]

npol = Polynomial([1, -1, 1, 0, -0.5, 1])
nderiv = npol.deriv()
nguess = 1.3 + 2j

print(apply_newtons_method_complex(pol, derivative=deriv, initial_guess=guess, iterations= 1))
print(num_apply_newtons_method_complex(npol, derivative=nderiv, initial_guess=nguess, iterations= 1))
