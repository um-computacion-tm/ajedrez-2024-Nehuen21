from game.pieza import Piece

class Queen(Piece):

    def __init__(self,color,position):
        super().__init__(color,position)
        
    def __str__(self,new_position):
        pass

    def check_move(self, positions, new_positions):
        result = False
