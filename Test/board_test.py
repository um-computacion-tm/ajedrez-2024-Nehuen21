import unittest
from  game.board import Board
from game.pieces.rook import Rook




class Test_setear_pieza(unittest.TestCase):

    def setUp(self) -> None:
        self.testboard = Board()


    def test_inicial(self):
        self.assertIsInstance(self.testboard.__positions__, list)        #Verifica que el elemento posiciones sea una lista
        self.assertEqual(self.testboard.__positions__[5][5], None)

    
    def Test_rook_black(self):
        self.assertEqual(self.testboard.__positions__[0][0].get_color, "black")
        self.assertEqual(self.testboard.__positions__[0][7].get_color, "black")

    def Test_rook_white(self):
        self.assertEqual(self.testboard.__positions__[0][7].get_color,"white")
        self.assertEqual(self.testboard.__positions__[7][7].get_color, "white")

    def Test_knight_white(self):
        self.assertEqual(self.testboard.__positions__[0][2].get_color,"white")
        self.assertEqual(self.testboard.__positions__[0][6].get_color, "white")

    def Test_knight_white(self):
        self.assertEqual(self.testboard.__positions__[7][2].get_color,"black")
        self.assertEqual(self.testboard.__positions__[7][6].get_color, "black")


    def test_obtn_pieza(self):
        self.assertIsInstance(self.tablerodeprueba.obtn_pieza(0,7),Rook)
        self.assertEqual(self.tablerodeprueba.obtn_pieza(4,4),None)
if __name__ == '__main__':
    unittest.main()