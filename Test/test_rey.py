import unittest
from game.rey import Rey
from game.board import Board
class TestRey(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__rey_blanco__ = Rey("blanco",0,4)
        self.__rey_negro__ = Rey("negro",7,4)
        self.__board__.setear_tablero(0,3,self.__rey_blanco__)

    def test_movimiento_valido_vertical(self):
        self.__board__._positions [1][4] = None
        resultado = self.__rey_blanco__.movimiento_valido(1, 4, self.__board__)
        self.assertTrue(resultado)
    
    def test_movimiento_valido_horizontal(self):
        self.__board__._positions [0][3] = None

        resultado = self.__rey_blanco__.movimiento_valido(0,3,self.__board__)
        self.assertTrue(resultado)

    def test_movimiento_valido_diagonal(self):
        self.__board__._positions [1][3] = None

        resultado = self.__rey_blanco__.movimiento_valido(1,3,self.__board__)
        self.assertTrue(resultado)

    def test_icono_rey_blanco(self):
       self.assertEqual(str(self.__rey_blanco__), "♔")

    def test_icono_rey_negro(self):
         self.assertEqual(str(self.__rey_negro__), "♚")

    def test_movimiento_invalido(self):
        resultado = self.__rey_blanco__.movimiento_valido(4,4,self.__board__)
        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()