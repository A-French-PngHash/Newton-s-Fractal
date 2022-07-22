import math

def get_exponential_form(real_part : float, imaginary_part : float) -> (float, float):
    """
    Get the trigonometric form of the given complex number
    :param real_part:
    :param imaginary_part:
    :return: The factor of the exponential, and the factor of the i power. ex : 5e^3i : (5, 3)
    """
    if round(real_part*10000000)/10000000 == 0 and round(imaginary_part*10000000)/10000000 == 0:
        return (0, 0)
    module = math.sqrt(real_part**2 + imaginary_part**2)
    if module == 0:
        print(real_part, imaginary_part)
    cos_output = real_part / module
    argument = math.acos(cos_output) # This is the argument.-
    if imaginary_part < 0:
        argument *= -1
    return (module, argument)

def get_algebric_form(module : float, argument : float) -> (float, float):
    """
    :param module:
    :param argument:
    :return: The real part, the imaginary part
    """
    real_part = math.cos(argument) * module
    imaginary_part = math.sin(argument) * module
    return(real_part, imaginary_part)

