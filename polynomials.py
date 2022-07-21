import math
import sympy
from sympy import I
from sympy.abc import x

import complex

pol = sympy.Poly(x**5 + x**2 -x + 0.2)
print(pol.eval(1 + I))

def derivate_polynomial(polynomial : dict) -> dict:
    """
    Derivate the given polynomial
    :param args: Factors where the key is the power of x and the element is the factor
    :return:
    """
    derivated_polynomial = {}
    for (power, factor) in polynomial.items():
        if power == 1:
            derivated_polynomial[0] = factor
        elif power != 0:
            derivated_polynomial[power - 1] = (power)*factor
    return derivated_polynomial

def calculate_image(polynomial : dict, input : float) -> float:
    """
    Calculates the image of the polynomial at the given x value.
    :param polynomial: Same form as for `derivate_polynomial`
    :param input: Real number
    :return: Image
    """
    output = 0
    for (power, factor) in polynomial.items():
        output += pow(input, power) * factor
    return output

poweer_of_i = [(0, 1), (-1, 0), (0, -1), (1, 0)]
"""The output when i is to the power of (index + 1).
First number is the real part, second is the imaginary.
"""

def calculate_image_complex(polynomial : dict, real_part : float, imaginary_part : float) -> tuple:
    """
    Calculates the image of the polynomial at the given x value.
    :param polynomial: Same form as for `derivate_polynomial`
    :param input: Complex number
    :return: Image
    """
    real_output = 0
    imaginary_output = 0

    module, argument = complex.get_exponential_form(real_part, imaginary_part)

    for (power, factor) in polynomial.items():
        if power == 0:
            real_output += factor
        elif power == 1:
            real_output += real_part * factor
            imaginary_output += imaginary_part * factor
        else:

            new_module = (module ** power) * factor
            new_argument = argument * power
            """
            5(x^2) where x is (3e^(2i))
            
            5 * (3^(2) * e^(2i)^2)
            5 * (9 * e^(2i * 2))
            45 * e^(4i)
            """
            nb_real_part, nb_imaginary_part = complex.get_algebric_form(new_module, new_argument)

            real_output += nb_real_part
            imaginary_output += nb_imaginary_part
    return real_output, imaginary_output