import unittest
from game.board import Board
from game.alfil import Alfil

class TestAlfil(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__alfil_blanco__ = Alfil("blanco",0,2)
        self.__alfil_negro__ = Alfil ("negro",7,5)

        self.__board__.setear_tablero(0,2,self.__alfil_blanco__)
        self.__board__.setear_tablero(7,5,self.__alfil_negro__)


    def test_icono_alfil_blanco(self):
       self.assertEqual(str(self.__alfil_blanco__), "♗")

    def test_icono_alfil_negro(self):
         self.assertEqual(str(self.__alfil_negro__), "♝")

    def test_movimiento_valido(self):
        resultado = self.__alfil_blanco__.movimiento_valido(1, 3, self.__board__)
        self.assertTrue(resultado)

    def test_movimiento_invalido(self):
  
        resultado = self.__alfil_blanco__.movimiento_valido(3, 0, self.__board__)
        self.assertFalse(resultado)




if __name__ == '__main__':
    unittest.main()
 

    