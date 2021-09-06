""" Probador de libreria de operaciones con numeros complejos imaginarios

"""

import Libreria_numeros_complejos as nc
import unittest

matrixc = [[(4, 2), (5, 4.6), (2.3, 5.7)], [(4.3, 5.7), (2, 6.2), (4, 6.8)]]
matrixc1 = [[(3, 7.1), (9, 10), (5, 3.5)], [(13, 15), (4, 16), (4, 12)]]

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
        self.assertEqual(nc.multi_escalar((4, 7.8) ,[(2, 3.5), (8.9, 5), (4, 9.2), (6, 2.3)]), [(-19.3, 29.6), (-3.4, 89.42), (-55.76, 68.0), (6.06, 56.0)])

    def test_sumamatrices(self):
        self.assertEqual(nc.suma_matricesc(matrixc, matrixc1), [[(-8.7, -9.3), (-2, -9.8), (0, -5.2)], [(-8.7, -9.3), (-2, -9.8), (0, -5.2)]])

    def test_negativam(self):
        self.assertEqual(nc.inversa_add_matrizc(matrixc1),[[(-3, -7.1), (-9, -10), (-5, -3.5)], [(-13, -15), (-4, -16), (-4, -12)]])

    def test_
if __name__ == '__main__':
    unittest.main()
