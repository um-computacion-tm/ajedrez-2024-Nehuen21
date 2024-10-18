from game.pieza import Pieza

class Rey(Pieza) : 
    def __init__(self,color,x,y):
        super().__init__(color,x,y)

    def __str__(self):
        return "♔" if self.__color__ == "blanco" else "♚"
    
    def movimiento_valido(self, x_nueva, y_nueva, board):
        """Valida el movimiento de una casilla del rey."""
        delta_x, delta_y = abs(self.__current_x__ - x_nueva), abs(self.__current_y__ - y_nueva)

        if max(delta_x, delta_y) == 1: 
            pieza_destino = board.obtener_pieza(x_nueva, y_nueva)
            return pieza_destino is None or pieza_destino.decime_color() != self.__color__

        return False
  