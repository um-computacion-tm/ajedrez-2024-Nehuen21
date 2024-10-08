import unittest

from game.board import Board

from game.reina import Reina

class TestReina(unittest.TestCase):
    
    def setUp(self):
        
        self.__board__ = Board()
        self.__reina_blanco__ = Reina("blanco",0,3)
        self.__reina_negro__ = Reina("negro",7,3)
        self.__board__.setear_tablero(0,3,self.__reina_blanco__)
        

    def test_movimiento_valido_diagonal(self):
        self.__board__._positions [1][2] = None
        resultado = self.__reina_blanco__.movimiento_valido(1, 2, self.__board__)
        self.assertTrue(resultado)

    def test_movimiento_valido_vertical(self):
        self.__board__._positions [2][2] = None

        resultado = self.__reina_blanco__.movimiento_valido(2,2,self.__board__)
        self.assertTrue(resultado)

    def test_movimiento_valido_horizontal(self):
        self.__board__._positions [0][2] = None
        resultado = self.__reina_blanco__.movimiento_valido(0, 2, self.__board__)
        self.assertTrue(resultado)

    def test_icono_blanco(self):
       self.assertEqual(str(self.__reina_blanco__), "♕")

    def test_icono_negro(self):
         self.assertEqual(str(self.__reina_negro__), "♛")


if __name__ == '__main__':
    unittest.main()