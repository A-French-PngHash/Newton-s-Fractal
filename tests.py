import unittest

import sympy
from sympy.abc import x

import newton_method


class TestNewton(unittest.TestCase):
    def test_classic_1(self):
        pol = sympy.Poly(x**5 + x**2 - x - 0.2)
        initial = 1.3
        iterations = 1
        result = newton_method.apply_newtons_method(pol, pol.diff(),  initial, iterations)
        self.assertAlmostEqual(result, 1.054, 3)

    def test_complex_1(self):
        pol = sympy.Poly(x ** 5 + x ** 2 - x - 0.2)
        initial = 1.3
        iterations = 1
        result = newton_method.apply_newtons_method(pol, pol.diff(), initial, iterations)
        self.assertAlmostEqual(result, 1.054, 3)
