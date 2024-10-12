from game.pieza import Pieza

class Rey(Pieza) : 
    def __init__(self,color,x,y):
        super().__init__(color,x,y)

    def __str__(self):
        return "♔" if self.__color__ == "blanco" else "♚"
    
    def movimiento_valido(self, x_nueva, y_nueva, board):
        delta_x = abs(self.__current_x__ - x_nueva)
        delta_y = abs(self.__current_y__ - y_nueva)

       
        if delta_x <= 1 and delta_y <= 1:
            pieza_destino = board.obtener_pieza(x_nueva, y_nueva)

            
            if pieza_destino is None or pieza_destino.decime_color() != self.__color__:
                return True
        return False   