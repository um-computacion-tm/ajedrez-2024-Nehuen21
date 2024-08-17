from piece import Piece


class Pawn(Piece):
    
    def __init__(self, position, color):
        super().__init__(position, color)
        self.has_moved = False
        self.can_en_passant = False
        self.promoted = False
        self.promotion_choice = None
        self.direction = 1 if color == 'white' else -1

    def move(self, new_position):
        # Lógica para mover el peón
        pass

    def promote(self, new_piece):
        # Lógica para promover el peón a otra pieza
        pass
