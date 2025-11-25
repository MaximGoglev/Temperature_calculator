import unittest
from Temperature_Calculator import (
    c_to_f, f_to_c, c_to_k, k_to_c,
    f_to_k, k_to_f)

class TemperatureTestCase(unittest.TestCase):
    # Цельсий - Фаренгей
    def test_c_to_f(self):
        self.assertAlmostEqual(c_to_f(0), 32)
        self.assertAlmostEqual(c_to_f(100), 212)
        self.assertAlmostEqual(c_to_f(-40), -40)
    
    def test_f_to_c(self):
        self.assertAlmostEqual(f_to_c(32), 0)
        self.assertAlmostEqual(f_to_c(212), 100)
        self.assertAlmostEqual(f_to_c(-40), -40)

    # Цельсий - Кельвин
    def test_c_to_k(self):
        self.assertAlmostEqual(c_to_k(0), 273.15)
        self.assertAlmostEqual(c_to_k(-273.15), 0)

    def test_k_to_c(self):
        self.assertAlmostEqual(k_to_c(273.15), 0)
        self.assertAlmostEqual(k_to_c(0), -273.15)

    # Фаренгейт - Кельвин
    def test_f_to_k(self):
        self.assertAlmostEqual(f_to_k(32), 273.15)
        self.assertAlmostEqual(f_to_k(-459.67), 0, places=2)
    
    def test_k_to_f(self):
        self.assertAlmostEqual(k_to_f(273.15), 32)
        self.assertAlmostEqual(k_to_f(0), -459.67, places=2)
    
    # Негативные тесты
    def test_extreme_values(self):
        # очень большие значения
        self.assertAlmostEqual(c_to_f(1e6), 1.8e6 + 32)
        self.assertAlmostEqual(f_to_c(1e6), (1e6 - 32) * 5 / 9)

    def test_below_absolute_zero(self):
        # физически невозможные значения
        self.assertLess(c_to_k(-274), 0)
        self.assertLess(f_to_k(-500), 0)

    def test_wrong_type(self):
        # передача строки должна вызвать TypeError
        with self.assertRaises(TypeError):
            c_to_f("abc")
        with self.assertRaises(TypeError):
            f_to_c(None)
        with self.assertRaises(TypeError):
            k_to_c("273.15")

if __name__ == '__main__':
    unittest.main()
