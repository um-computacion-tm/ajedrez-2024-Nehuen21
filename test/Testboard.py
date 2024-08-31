# tests/test_board.py

import unittest
from Game.board import Board

class TestBoard(unittest.TestCase):
    
    def test_initialization(self):
        board = Board(for_test=True)  # Usamos for_test=True para no colocar piezas
        self.assertEqual(len(board._Board__positions__), 8)
        for row in board._Board__positions__:
            self.assertEqual(len(row), 8)
            self.assertTrue(all(cell is None for cell in row))

if __name__ == '__main__':
    unittest.main()
