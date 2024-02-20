import unittest
from calculatrice import Calculatrice

class TestCalculatrice(unittest.TestCase): # TestXXXX
    def test_addition(self):
        calc1 = Calculatrice(1, 2)
        self.assertEqual(calc1.addition(), 3)

        calc2 = Calculatrice(1.5, 2.5)
        self.assertTrue(calc2.addition() == 4)

    def test_division(self):
        calc1 = Calculatrice(4, 2)
        self.assertEqual(calc1.division(), 2)

        calc2 = Calculatrice(10, 0)
        self.assertTrue(calc2.division() == "Erreur")

if __name__ == '__main__':
    unittest.main()