import unittest
from game.board import Board
from game.torre import Torre

class TestTorre(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__torre_blanco__ = Torre("blanco",0,2)
        self.__torre_negro__ = Torre ("negro",7,7)

        self.__board__.setear_tablero(0,2,self.__torre_blanco__)
        self.__board__.setear_tablero(7,7,self.__torre_negro__)


    def test_icono_torre_blanco(self):
       self.assertEqual(str(self.__torre_blanco__), "♖")

    def test_icono_torre_negro(self):
         self.assertEqual(str(self.__torre_negro__), "♜")

    def test_movimiento_valido_vertical(self):
        self.__board__._positions [0][4] = None
        resultado = self.__torre_blanco__.movimiento_valido(0, 4, self.__board__)
        
        self.assertTrue(resultado)

    def test_movimiento_invalido_(self):
  
        self.__board__.setear_tablero(2, 2, self.__torre_blanco__)  
        resultado = self.__torre_blanco__.movimiento_valido(3, 3, self.__board__)
        
        self.assertFalse(resultado)

    
    def test_movimiento_valido_horizontal(self):
        self.__board__._positions [0][5] = None
        resultado = self.__torre_blanco__.movimiento_valido(0,6 , self.__board__)

        self.assertTrue(resultado)


if __name__ == '__main__':
    unittest.main()
   