import unittest
from find_quadratic_equation_solutions import raices

class TestQuadraticRoots(unittest.TestCase):
    def test_two_real_roots(self):
        resultado = raices(1, -3, 2)
        self.assertEqual(resultado, (2.0, 1.0))

    def test_no_real_roots(self):
        resultado = raices(1, 0, 5)
        self.assertEqual(resultado, "No hay soluciones reales")

if __name__ == '__main__':
    unittest.main()