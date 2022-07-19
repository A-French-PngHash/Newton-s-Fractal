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

def calculate_image(polynomial : dict, input : int):
    """
    Calculates the image of the polynomial at the given x value.
    :param polynomial: Same form as for `derivate_polynomial`
    :param input:
    :return:
    """
    output = 0
    for (power, factor) in polynomial.items():
        output += pow(input, power) * factor
    return output

