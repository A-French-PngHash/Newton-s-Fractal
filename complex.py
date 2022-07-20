import math

def get_exponential_form(real_part : float, imaginary_part : float) -> (float, float):
    """
    Get the trigonometric form of the given complex number
    :param real_part:
    :param imaginary_part:
    :return: The factor of the exponential, and the factor of the i power. ex : 5e^3i : (5, 3)
    """
    if real_part == 0 and imaginary_part == 0:
        return (0, 0)
    module = math.sqrt(real_part**2 + imaginary_part**2)
    cos_output = real_part / module
    cos_input = math.acos(cos_output) # This is the argument.
    return (module, cos_input)

def get_algebric_form(module : float, argument : float) -> (float, float):
    """
    :param module:
    :param argument:
    :return: The real part, the imaginary part
    """
    real_part = math.cos(argument) * module
    imaginary_part = math.sin(argument) * module
    return(real_part, imaginary_part)

