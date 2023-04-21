import unittest

class Etape5(unittest.TestCase):
    def test_anneau_mult(self):
        import Galois
        anneau = Galois.AnneauPolynome(Galois.CorpsGalois(285))
        in_outs = [
            (([], []), []),
            (([1], []), []),
            (([], [1]), []),
            (([1], [1]), [1]),
            (([3], [3]), [5]),
            (([3], [2]), [6]),
            (([1, 3], [4, 5]), [4, 9, 15]),
        ]
        for (a, b), r in in_outs:
            self.assertEqual(anneau.fois(a, b), r,
                "La multiplication des polynômes {} et {} "
                "ne donne pas le résultat attendu".format(a, b))
    
    def test_reste_division(self):
        import Galois
        anneau = Galois.AnneauPolynome(Galois.CorpsGalois(285))
        in_outs = [
            (([], [1]), []),
            (([1], [1]), []),
            (([1], [2]), []),
            (([1, 1, 1, 1, 1], [1, 1, 1, 1]), [0, 0, 1]),
            (([45, 12, 17], [34, 22]), [181]),
        ]
        for (a, b), r in in_outs:
            self.assertEqual(anneau.reste_division(a, b), r,
                "La division des polynômes {} par {} "
                "ne donne pas le reste attendu".format(a, b))
    
    def test_generateur(self):
        import Galois
        anneau = Galois.AnneauPolynome(Galois.CorpsGalois(285))
        in_outs = [
            (2, [1, 3, 2]),
            (7, [1, 127, 122, 154, 164, 11, 68, 117]),
            (10, [1, 216, 194, 159, 111, 199, 94, 95, 113, 157, 193]),
            (13, [1, 137, 73, 227, 17, 177, 17, 52, 13, 46, 43, 83, 132, 120]),
            (17, [1, 119, 66, 83, 120, 119, 22, 197, 83, 249, 41, 143, 134, 85, 53, 125, 99, 79]),
        ]

        for i, r in in_outs:
            self.assertEqual(anneau.generateur(i), r,
                "Le générateur {} n'est pas le bon".format(i))

class Etape4(unittest.TestCase):
    
    def test_corps_addition(self):
        in_outs = [
            ((1, 2), 3),
            ((1, 1), 0),
            ((19, 19), 0),
            ((10, 12), 6),
        ]

        import Galois
        corps = Galois.CorpsGalois(285)

        for (a, b), r in in_outs:
            self.assertEqual(corps.plus(a, b), r,
                "L'addition des polynomes {:08b} et {:08b} "
                "ne donne pas le résultat attendu".format(a, b))

    def test_corps_multiplication(self):
        in_outs = [
            ((1, 2), 2),
            ((1, 1), 1),
            ((19, 19), 24),
            ((10, 12), 120),
            ((220, 134), 192),
            ((134, 220), 192),
            ((255, 255), 226),
            ((0, 14), 0),
            ((14, 0), 0),
        ]

        import Galois
        corps = Galois.CorpsGalois(285)

        for (a, b), r in in_outs:
            self.assertEqual(corps.fois(a, b), r,
                "L'addition des polynomes {:08b} et {:08b} "
                "ne donne pas le résultat attendu".format(a, b))

    def test_corps_division(self):
        in_outs = [
            ((1, 1), 1),
            ((19, 19), 1),
            ((120, 12), 10),
            ((1, 2), 142),
            ((192, 220), 134),
            ((192, 134), 220),
            ((0, 14), 0),
        ]

        import Galois
        corps = Galois.CorpsGalois(285)

        for (a, b), r in in_outs:
            self.assertEqual(corps.division(a, b), r,
                "La division du polynome {:08b} par le polynome {:08b} "
                "ne donne pas le résultat attendu".format(a, b))

    def test_corps_puissance(self):
        in_outs = [
            ((1, 1), 1),
            ((19, 0), 1),
            ((167, 1), 167),
            ((1, 14), 1),
            ((2, 2), 4),
            ((3, 3), 15),
            ((2, 4), 16),
            ((2, 5), 32),
            ((2, 7), 128),
            ((2, 8), 29),
            ((2, 9), 58),
            ((2, 12), 205),
            ((255, 100), 230)
        ]

        import Galois
        corps = Galois.CorpsGalois(285)

        for (a, b), r in in_outs:
            self.assertEqual(corps.puissance(a, b), r,
                "La puissance {} du polynome {:08b} "
                "ne donne pas le résultat attendu".format(b, a))
        


if __name__ == "__main__":
    unittest.main()