from piece import Piece

class King(Piece):

    def __init__(self,posicion_inicial,color):
        self.posicion_actual = posicion_inicial
        self.color = color
        self.movimientos = 0
        self.en_jake = False

def mover(self, posicion_destino):
        if self.es_movimiento_legal(posicion_destino):
            self.posicion_actual = posicion_destino
            self.movimientos += 1
            
        else:
            raise ValueError("Movimiento ilegal para el rey.")