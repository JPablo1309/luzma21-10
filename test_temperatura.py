import unittest
from main import celsius_a_fahrenheit, fahrenheit_a_celsius

class TestConversorTemperatura(unittest.TestCase):

    def test_celsius_a_fahrenheit(self):
        # Prueba unitaria: comprobar una conversión específica
        self.assertAlmostEqual(celsius_a_fahrenheit(0), 32)
        self.assertAlmostEqual(celsius_a_fahrenheit(100), 212)

    def test_fahrenheit_a_celsius(self):
        self.assertAlmostEqual(fahrenheit_a_celsius(32), 0)
        self.assertAlmostEqual(fahrenheit_a_celsius(212), 100)

if __name__ == "__main__":
    unittest.main()
