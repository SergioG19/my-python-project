import unittest
from app import saludo

class TestSaludo(unittest.TestCase):
    def test_saludo(self):
        self.assertEqual(saludo("Mundo"), "Hola, Mundo!")

if __name__ == '__main__':
    unittest.main()
