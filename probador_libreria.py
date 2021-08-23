""" Probador de libreria de operaciones con numeros complejos imaginarios

"""

import Libreria_numeros_complejos as nc
import unittest


class Library_test(unittest.TestCase):

    def test_sumac(self):
        self.assertEqual(nc.suma_complejos([12, -3.5], [4, 7.8]), [16, 4.3])

    def test_restac(self):
        self.assertEqual(nc.resta_complejos([12, -3.5], [4, 7.8]), [8, -11.3])

    def test_multic(self):
        self.assertEqual(nc.multiplicacion_complejos([12, -3.5], [4, 7.8]), [75.3, 79.6])

    def test_divic(self):
        self.assertEqual(nc.division_complejos([12, -3.5], [4, 7.8]), [0.27, -1.4])

    def test_module(self):
        self.assertEqual(nc.modulo_complejos([12, -3.5]), 12.5)

    def test_conjugado(self):
        self.assertEqual(nc.conjugado_complejos([4, 7.8]), [4, -7.8])

    def test_rpolar(self):
        self.assertEqual(nc.rep_polar([5, 6.21]), [7.97, 0.89])

    def test_rcar(self):
        self.assertEqual(nc.rep_cartesiana([7.97, 0.89]), [5.02, 6.19])

    def test_multip(self):
        self.assertEqual(nc.multiplicacion_polar([7.97, 0.89], [12.5, -0.28]), [99.62, 0.61])

    def test_divip(self):
        self.assertEqual(nc.division_polar([12.5, -0.28], [8.76, 1.09]), [1.43, -1.37])

    def test_potenciap(self):
        self.assertEqual(nc.potencia_polar([99.62, 0.61], 3), [988643.27, 1.83])

if __name__ == '__main__':
    unittest.main()
