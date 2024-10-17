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
        
        resultado = self.__reina_blanco__.movimiento_valido(1, 2, self.__board__)
        self.assertTrue(resultado)

    def test_movimiento_valido_vertical(self):
       

        resultado = self.__reina_blanco__.movimiento_valido(2,3,self.__board__)
        self.assertTrue(resultado)

    def test_movimiento_valido_horizontal(self):
        
        resultado = self.__reina_blanco__.movimiento_valido(0, 2, self.__board__)
        self.assertTrue(resultado)

    def test_icono_reina_blanco(self):
       self.assertEqual(str(self.__reina_blanco__), "♕")

    def test_icono_reina_negro(self):
         self.assertEqual(str(self.__reina_negro__), "♛")

    def test_movimiento_invalido(self):
        resultado = self.__reina_blanco__.movimiento_valido(3,1,self.__board__)
        self.assertFalse(resultado)


if __name__ == '__main__':
    unittest.main()