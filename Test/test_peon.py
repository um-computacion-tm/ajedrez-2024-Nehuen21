import unittest
from game.board import Board
from game.peon import Peon

class TestPeon(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.__peon_negro__ = Peon("negro", 6, 3)
        self.__peon_blanco__ = Peon("blanco", 1, 3)
        self.board.setear_tablero(6, 3, self.__peon_negro__)
        self.board.setear_tablero(1, 3, self.__peon_blanco__)

    def test_movimiento_valido_una_casilla_adelante(self):
        resultado = self.__peon_blanco__.movimiento_valido(2, 3, self.board)
        self.assertTrue(resultado)

    
    def test_movimiento_valido_diagonal(self):
        
        self.board.setear_tablero(5, 2, Peon("blanco", 5, 2))
        resultado = self.__peon_negro__.movimiento_valido(5, 2, self.board)
        self.assertTrue(resultado)

    def test_movimiento_invalido_sin_captura_diagonal(self):
        resultado = self.__peon_blanco__.movimiento_valido(3, 5, self.board)
        self.assertFalse(resultado)

    def test_iconos(self):
        self.assertEqual(str(self.__peon_blanco__), "♙")
        self.assertEqual(str(self.__peon_negro__), "♟")

if __name__ == "__main__":
    unittest.main()
