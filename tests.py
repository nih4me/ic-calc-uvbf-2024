import unittest
from .calculatrice import Calculatrice

class CalculatriceTest(unittest.TestCase):
    def test_addition(self):
        calc1 = Calculatrice(1, 2)
        self.assertEqual(calc1.addition(), 3)

        calc2 = Calculatrice(1.5, 2.5)
        self.assertTrue(calc2.addition() == 4)