import unittest
from game.board import Board
from game.peon import Peon

class TestPeon(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.__peon_negro__ = Peon("negro", 6, 3)  
        self.__peon_blanco__ = Peon("blanco", 1, 3)   
        self.board.setear_tablero( 6, 3, self.__peon_negro__)
        self.board.setear_tablero( 1, 3, self.__peon_blanco__)

 
    def test_movimientos_peon(self):
        movimientos_validos = [(3, 3), (2, 3)]
        movimientos_invalidos = [(4, 3), (3, 5)]

        for x, y in movimientos_validos:
            with self.subTest(f"Moviendo a {x}, {y}"):
                resultado = self.__peon_blanco__.movimiento_valido(x, y, self.board)
                self.assertTrue(resultado)

        for x, y in movimientos_invalidos:
            with self.subTest(f"Movimiento inválido a {x}, {y}"):
                resultado = self.__peon_blanco__.movimiento_valido(x, y, self.board)
                self.assertFalse(resultado)

   
        
    def test_iconos(self):
       self.assertEqual(str(self.__peon_blanco__), "♙")          
       self.assertEqual(str(self.__peon_negro__), "♟")  

    

    

if __name__ == "__main__":
    unittest.main()
