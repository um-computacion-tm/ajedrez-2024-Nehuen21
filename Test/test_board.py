import unittest
from game.torre import Torre
from game.board import Board
from game.caballo import Caballo
from game.alfil import Alfil
from game.rey import Rey

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()  # Quitamos los dobles guiones bajos
        self.board.setear_piezas()

    def test_obtener_torre_blanca(self):
        torre = self.board.obtener_pieza(0, 0)  # También sin dobles guiones bajos
        self.assertIsInstance(torre, Torre)

    def test_obtener_torre_negra(self):

        torre = self.board.obtener_pieza(7, 7)  
        self.assertIsInstance(torre, Torre)

    def test_obtener_caballo_negro(self):

        caballo = self.board.obtener_pieza(0,1)  
        self.assertIsInstance(caballo, Caballo)

    def test_obtener_caballo_blanco(self):

        caballo = self.board.obtener_pieza(7,1)  
        self.assertIsInstance(caballo, Caballo)

    def test_obtener_alfil_negro(self):

        alfil = self.board.obtener_pieza(0,2)  
        self.assertIsInstance(alfil, Alfil)

    def test_obtener_alfil_blanco(self):

        alfil = self.board.obtener_pieza(7,2)  
        self.assertIsInstance(alfil, Alfil)

    def test_obtener_pieza(self):
        self.assertIsInstance(self.board.obtener_pieza(0,4),Rey)
        self.assertEqual(self.board.obtener_pieza(5,4),None)

        


    

if __name__ == '__main__':
    unittest.main()
