import unittest

from game.board import Board
from game.chess import Ajedres
from game.torre import Torre

class TestChess(unittest.TestCase):

    def setUp(self):
        self.__ajedres__=Ajedres()
        self.__board__ = Board()
        


    def testPiezaInexistente(self):
         """Verifica que se lance una excepción si no hay pieza en la posición."""
         with self.assertRaises(Exception):
             self.__ajedres__.obtener_pieza_origen(3,3)

    def test_turno_actual_inicial(self):
        self.assertEqual(self.__ajedres__.turno_actual(),"BLANCO")

    def test_cambio_de_turno(self):
        self.__ajedres__.cambio_de_turno()

        self.assertEqual(self.__ajedres__.turno_actual(),"NEGRO")

        self.__ajedres__.cambio_de_turno()
        self.assertEqual(self.__ajedres__.turno_actual(),"BLANCO")

    

    
if __name__ == "__main__":
    unittest.main()
