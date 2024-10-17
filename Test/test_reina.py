import unittest
from game.board import Board
from game.reina import Reina

class TestReina(unittest.TestCase):
    
    def setUp(self):
        
        self.__board__ = Board()
        self.__reina_blanco__ = Reina("blanco",0,3)
        self.__reina_negro__ = Reina("negro",7,3)
        self.__board__.setear_tablero(0,3,self.__reina_blanco__)
        

    def test_reina_movimiento_diagonal_valido(self):
        """Valida un movimiento diagonal permitido para la reina."""
        destino = (1, 2)
        self.assertTrue(
            self.__reina_blanco__.movimiento_valido(*destino, self.__board__))
    
    
    
    
    def test_reina_movimiento_vertical_valido(self):
        """Valida un movimiento vertical permitido para la reina."""
        destino = (2, 3)
        self.assertTrue(
            self.__reina_blanco__.movimiento_valido(*destino, self.__board__))



    def test_reina_movimiento_horizontal_valido(self):
        """Valida un movimiento horizontal permitido para la reina."""
        destino = (0, 2)
        self.assertTrue(
            self.__reina_blanco__.movimiento_valido(*destino, self.__board__))


    def test_reina_movimiento_invalido(self):
        """Verifica que la reina no pueda realizar un movimiento ilegal."""
        destino = (3, 1)
        self.assertFalse(
            self.__reina_blanco__.movimiento_valido(*destino, self.__board__))



    def test_icono_reina_blanco(self):
       self.assertEqual(str(self.__reina_blanco__), "♕")

    def test_icono_reina_negro(self):
         self.assertEqual(str(self.__reina_negro__), "♛")

    


if __name__ == '__main__':
    unittest.main()