import unittest
from game.rey import Rey
from game.board import Board
class TestRey(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__rey_blanco__ = Rey("blanco",0,4)
        self.__rey_negro__ = Rey("negro",7,4)
        self.__board__.setear_tablero(0,4,self.__rey_blanco__)
        self.__board__.setear_tablero(7, 4, self.__rey_negro__)

    def test_movimiento_valido(self):
        valid_moves = [
            (1, 4),  
            (0, 5),  
            (0, 3),  
            (1, 5), 
            (1, 3),  
        ]
        
        for move in valid_moves:
            resultado = self.__rey_blanco__.movimiento_valido(move[0], move[1], self.__board__)
            self.assertTrue(resultado)

    def test_movimiento_invalido(self):
     
        invalid_moves = [
            (2, 4),  
            (0, 6),  
            (2, 6),  
        ]
        
        for move in invalid_moves:
            resultado = self.__rey_blanco__.movimiento_valido(move[0], move[1], self.__board__)
            self.assertFalse(resultado)

    def test_icono_rey_blanco(self):
       self.assertEqual(str(self.__rey_blanco__), "♔")

    def test_icono_rey_negro(self):
         self.assertEqual(str(self.__rey_negro__), "♚")

    

if __name__ == '__main__':
    unittest.main()