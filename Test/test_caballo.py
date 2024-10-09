import unittest

from game.board import Board
from game.caballo import Caballo

class TestCaballo(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__caballo_blanco__ = Caballo("blanco",3,3 )                #Inicializo el caballo en el medio del tablero para mayor claridad en los movimientos
        self.__cabalo_negro__ = Caballo("negro",7,1)

        self.__board__.setear_tablero(3,3,self.__caballo_blanco__)

    def test_movimiento_valido__vertical_derecha(self):
        self.__board__._positions [5] [4] = None
        resultado = self.__caballo_blanco__.movimiento_valido(5,4,self.__board__)

        self.assertTrue(resultado)
    def test_movimiento_valido_arriba_izquierda(self):
        resultado = self.__caballo_blanco__.movimiento_valido(5,2,self.__board__)
        self.assertTrue(resultado)
    
    def test_movimiento_valido_horizontal_izquierda_(self):
        resultado = self.__caballo_blanco__.movimiento_valido(4,1,self.__board__)
        self.assertTrue(resultado)

    def test_movimiento_valido_horizontal_derecha_(self):
        resultado = self.__caballo_blanco__.movimiento_valido(4,5,self.__board__)
        self.assertTrue(resultado)


    def test_movimiento_invalido(self):
        resultado = self.__caballo_blanco__.movimiento_valido(4,4,self.__board__)
        self.assertFalse(resultado)

    def test_icono_caballlo_blanco(self):
       self.assertEqual(str(self.__caballo_blanco__), "♘")

    def test_icono_caballo_negro(self):
         self.assertEqual(str(self.__cabalo_negro__), "♞")


if __name__ == '__main__':
    unittest.main()
