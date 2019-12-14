import unittest
import kalkulator

class testy_kalkulator(unittest.TestCase):

    def test_dodawanie(self):
        wynik = kalkulator.dodaj(2,3)
        self.assertEqual(wynik, 5)

    def test_odejmowanie(self):
        wynik = kalkulator.odejmij(3,2)
        self.assertEqual(wynik, 1)

    def test_mnozenie(self):
        wynik = kalkulator.mnoz(2,3)
        self.assertEqual(wynik, 6)

    def test_dzielenie(self):
        wynik = kalkulator.dziel(3,2)
        self.assertEqual(wynik, 1,5)

if __name__ == '__main__' :
    unittest.main()
