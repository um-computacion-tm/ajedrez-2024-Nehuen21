from game.pieza import Piece

class Torre(Piece):
    def __init__(self, color, posicion):
        super().__init__(color, posicion)

    def move(self,new_position):
        pass

