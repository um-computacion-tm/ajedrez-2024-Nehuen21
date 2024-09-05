from piece import Piece


class Pawn(Piece):
    
    def __init__(self,color, position,):
        super().__init__(color,position)
        self.has_moved = False
        

    def move(self, new_position):
        # Lógica para mover el peón
        pass

    def promote(self, new_piece):
        # Lógica para promover el peón a otra pieza
        pass
