import unittest
from numpy.polynomial import Polynomial
import newton_method


class TestNewton(unittest.TestCase):

    def test_classic(self):
        pol = Polynomial([-0.2, -1, 1, 0, 0, 1])
        print(pol)
        initial = 1.3
        iterations = 1
        result = newton_method.apply_newtons_method(pol,pol.deriv(),  initial, iterations)
        self.assertAlmostEqual(result, 1.054, 3)

    def test_complex(self):
        pol = Polynomial([1, -1, 1, 0, 0, 1])
        initial = -0.5 + 0.5j
        iterations = 1
        result = newton_method.apply_newtons_method_complex(pol, pol.deriv(), initial, iterations)
        self.assertAlmostEqual(result.real, 0.054, 3)
        self.assertAlmostEqual(result.imag, 0.324, 3)

    def test_classic_multi_iterations(self):
        pol = Polynomial([-0.2, -1, 1, 0, 0, 1])
        initial = 1.3
        iterations = 4
        result = newton_method.apply_newtons_method(pol, pol.deriv(), initial, iterations)
        self.assertAlmostEqual(result, 0.812, 3)

    def test_complex_multi_iterations(self):
        pol = Polynomial([1, -1, 1, 0, 0, 1])
        initial = -0.5 + 0.5j
        iterations = 6
        result = newton_method.apply_newtons_method_complex(pol, pol.deriv(), initial, iterations)
        self.assertAlmostEqual(result.real, 0.662, 3)
        self.assertAlmostEqual(result.imag, 0.562, 3)
