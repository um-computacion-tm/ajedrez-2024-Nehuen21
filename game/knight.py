from game.pieza import Piece
class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        
    def move(self,new_position):
        pass