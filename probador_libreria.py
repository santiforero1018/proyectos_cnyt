""" Probador de libreria de operaciones con numeros complejos imaginarios

"""

import math
import Libreria_numeros_complejos as nc
import unittest

raiz = math.sqrt(2)

class Library_test(unittest.TestCase):

    def test_sumac(self):
        self.assertEqual(nc.suma_complejos((12, -3.5), (4, 7.8)), (16, 4.3))

    def test_restac(self):
        self.assertEqual(nc.resta_complejos((12, -3.5), (4, 7.8)), (8, -11.3))

    def test_multic(self):
        self.assertEqual(nc.multiplicacion_complejos((12, -3.5), (4, 7.8)), (75.3, 79.6))

    def test_divic(self):
        self.assertEqual(nc.division_complejos((12, -3.5), (4, 7.8)), (0.27, -1.4))

    def test_module(self):
        self.assertEqual(nc.modulo_complejos((12, -3.5)), 12.5)

    def test_conjugado(self):
        self.assertEqual(nc.conjugado_complejos((4, 7.8)), (4, -7.8))

    def test_rpolar(self):
        self.assertEqual(nc.rep_polar((5, 6.21)), (7.97, 0.89))

    def test_rcar(self):
        self.assertEqual(nc.rep_cartesiana((7.97, 0.89)), (5.02, 6.19))

    def test_multip(self):
        self.assertEqual(nc.multiplicacion_polar((7.97, 0.89), (12.5, -0.28)), (99.62, 0.61))

    def test_divip(self):
        self.assertEqual(nc.division_polar((12.5, -0.28), (8.76, 1.09)), (1.43, -1.37))

    def test_potenciap(self):
        self.assertEqual(nc.potencia_polar((99.62, 0.61), 3), (988643.27, 1.83))

    def test_sumavec(self):
        self.assertEqual(
            nc.suma_vectorescpx([(2, 3.5), (8.9, 5), (4, 9.2), (6, 2.3)], [(2.3, 6), (7.4, 8), (3, 3.8), (4, 2.5)]), [(4.3, 9.5), (16.3, 13), (7, 13.0), (10, 4.8)])

    def test_inversev(self):
        self.assertEqual(nc.inverse_vectorcx([(2, 3.5), (8.9, 5), (4, 9.2), (6, 2.3)]), [(-2, -3.5), (-8.9, -5), (-4, -9.2), (-6, -2.3)])

    def test_multescalarv(self):
        self.assertEqual(nc.multi_escalar((4, 7.8), [(2, 3.5), (8.9, 5), (4, 9.2), (6, 2.3)]), [(-19.3, 29.6), (-3.4, 89.42), (-55.76, 68.0), (6.06, 56.0)])

    def test_negativam(self):
        self.assertEqual(nc.inversa_add_matrizc([[(3, 7), (9, 10), (5, 3)], [(13, 15), (4, 16), (4, 12)]]), [[(-3, -7), (-9, -10), (-5, -3)], [(-13, -15), (-4, -16), (-4, -12)]])

    def test_sumamatrices(self):
        self.assertEqual(nc.suma_matricesc([[(3, 7), (9, 10), (5, 3)], [(13, 15), (4, 16), (4, 12)]], [[(4, 2), (5, 4.6), (2.3, 5.7)], [(4.3, 5.7), (2, 6.2), (4, 6.8)]]), [[(17.3, 20.7), (6, 22.2), (8, 18.8)], [(17.3, 20.7), (6, 22.2), (8, 18.8)]])

    def test_multiescalarm(self):
        self.assertEqual(nc.multiescalar_matrix((4, 7.8), [[(3, 7), (9, 10), (5, 3)], [(13, 15), (4, 16), (4, 12)]]), [[(-42.6, 51.4), (-42.0, 110.2), (-3.4, 51.0)], [(-65.0, 161.4), (-108.8, 95.2), (-77.6, 79.2)]])

    def test_transpuesta(self):
        self.assertEqual(nc.transpuesta([[(4, 2), (5, 4.6), (2.3, 5.7)], [(4.3, 5.7), (2, 6.2), (4, 6.8)]]), [[(4, 2), (4.3, 5.7)], [(5, 4.6), (2, 6.2)], [(2.3, 5.7), (4, 6.8)]])

    def test_conjugadov(self):
        self.assertEqual(nc.conjugadov([(2, 3.5), (8.9, 5), (4, 9.2), (6, 2.3)]), [(2, -3.5), (8.9, -5), (4, -9.2), (6, -2.3)])

    def test_conjugadom(self):
        self.assertEqual(nc.conjugadom([[(2, -1), (4, 1), (9, 3)], [(8, -6), (7, 6), (4, -1)], [(9, 3), (8, -6), (4, 1)]]), [[(2, 1), (4, -1), (9, -3)], [(8, 6), (7, -6), (4, 1)], [(9, -3), (8, 6), (4, -1)]])

    def test_adjunta(self):
        self.assertEqual(nc.adjunta([[(4, 2), (5, 4.6), (2.3, 5.7)], [(4.3, 5.7), (2, 6.2), (4, 6.8)]]), [[(4, -2), (4.3, -5.7)], [(5, -4.6), (2, -6.2)], [(2.3, -5.7), (4, -6.8)]])

    def test_multima(self):
        self.assertTrue(nc.multiplicacion_matrices([[(4, 2), (5, 4.6), (2.3, 5.7)], [(4.3, 5.7), (2, 6.2), (4, 6.8)]], [[(2, -1), (4, 1), (9, 3)], [(8, -6), (7, 6), (4, -1)], [(9, 3), (8, -6), (4, 1)]]), [[(81.2, 65.0), (74.0, 106.0), (58.1, 68.5)], [(83.1, 117.9), (61.1, 112.9), (45.0, 118.2)]])
        self.assertFalse(nc.multiplicacion_matrices([[(4, 2), (5, 4.6), (2.3, 5.7)], [(4.3, 5.7), (2, 6.2), (4, 6.8)]], [[(3, 7.1), (9, 10), (5, 3.5)], [(13, 15), (4, 16), (4, 12)]]))

    def test_accionmv(self):
        self.assertEqual(nc.accionmatriz_vector([[(2, -1), (4, 1)], [(8, -6), (7, 6)]], [(4.0, -1.8), (9.0, 3.0)]), [(78.0, 7.2), (195.0, 18.0)])

    def test_productoint(self):
        self.assertEqual(nc.int_product([(4.0, -1.8), (9.0, 3.0)], [(3.0, 7.8), (8.7, 5.2)]), (91.86, 57.3))

    def test_norma(self):
        self.assertEqual(nc.norma_vector([(2.3, 6), (7.4, 8), (3, 3.8), (4, 2.5)]), 192.13)

    def test_distancia(self):
        self.assertEqual(nc.distanciav([(3.0, 7.8), (8.7, 5.2)], [(4.0, -1.8), (9.0, 3.0)]), 98.08)

    def test_unitaria(self):
        self.assertTrue(nc.unitaria([[(0, 1/raiz), (0,-1/raiz)], [(0, 1/raiz), (0, 1/raiz)]]))
        self.assertFalse(nc.unitaria([[(3, 7.1), (9, 10), (5, 3.5)], [(13, 15), (4, 16), (4, 12)]]))

    def test_hermitiana(self):
        self.assertTrue(nc.hermitiana([[(-1, 0), (0, -1)], [(0, 1), (1, 0)]]))
        self.assertFalse(nc.hermitiana([[(3, 7.1), (9, 10), (5, 3.5)], [(13, 15), (4, 16), (4, 12)]]))

    def test_tensorpv(self):
        self.assertEqual(nc.tensor_productv([(3, 5), (4, 6.3), (7, 2.8)], [(-1, 4), (2, 7.2)]), [(-23, 7), (-30.0, 31.6), (-29.2, 9.7), (-37.36, 41.4), (-18.2, 25.2), (-6.16, 56.0)])


if __name__ == '__main__':
    unittest.main()
