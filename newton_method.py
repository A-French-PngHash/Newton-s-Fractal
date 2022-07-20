import operations
import polynomials


def apply_newtons_method(polynomial : dict, derivative : dict,  initial_guess : float, iterations : float):
    new_guess = initial_guess
    for i in range(iterations):
        step = - (polynomials.calculate_image(polynomial, new_guess) / polynomials.calculate_image(derivative, new_guess))
        new_guess += step
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
