import unittest

import sympy
from sympy.abc import x

import newton_method


class TestNewton(unittest.TestCase):

    def test_classic(self):
        pol = sympy.Poly(x**5 + x**2 - x - 0.2)
        initial = 1.3
        iterations = 1
        result = newton_method.apply_newtons_method(pol, pol.diff(),  initial, iterations)
        self.assertAlmostEqual(result, 1.054, 3)

    def test_complex(self):
        pol = sympy.Poly(x ** 5 + x ** 2 - x + 1)
        initial = (-0.5, 0.5)
        iterations = 1
        result = newton_method.apply_newtons_method_complex(pol, pol.diff(), initial, iterations)
        self.assertAlmostEqual(result[0], 0.054, 3)
        self.assertAlmostEqual(result[1], 0.324, 3)

    def test_classic_multi_iterations(self):
        pol = sympy.Poly(x ** 5 + x ** 2 - x - 0.2)
        initial = 1.3
        iterations = 4
        result = newton_method.apply_newtons_method(pol, pol.diff(), initial, iterations)
        self.assertAlmostEqual(result, 0.812, 3)

    def test_complex_multi_iterations(self):
        pol = sympy.Poly(x ** 5 + x ** 2 - x + 1)
        initial = (-0.5, 0.5)
        iterations = 6
        result = newton_method.apply_newtons_method_complex(pol, pol.diff(), initial, iterations)
        self.assertAlmostEqual(result[0], 0.662, 3)
        self.assertAlmostEqual(result[1], 0.562, 3)
