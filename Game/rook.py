from piece import Piece

class Rook(Piece):
    def __init__(self, posicion_inicial, color):
        self.posicion_actual = posicion_inicial
        self.color = color
        self.movimientos = 0
        self.enroque_disponible = True
    
