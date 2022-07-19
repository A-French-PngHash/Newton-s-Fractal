import polynomials


def apply_newtons_method(polynomial : dict, initial_guess : int, iterations : int):
    new_guess = initial_guess
    for i in range(iterations):
        derivative = polynomials.derivate_polynomial(polynomial)
        step = - (polynomials.calculate_image(polynomial, new_guess) / polynomials.calculate_image(derivative, new_guess))
        new_guess += step
    return new_guess


test_polynomial = {5 : 1, 2 : 1, 1 : -1, 0 : -0.2}
print(apply_newtons_method(test_polynomial, 1.3, 5))
