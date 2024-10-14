from game.pieza import Pieza

class Peon(Pieza):
    def __init__(self,color,x,y):
        super().__init__(color,x,y)

    def __str__(self):
        return "♙" if self.__color__ == "blanco" else "♟"

    def movimiento_valido(self,x_nueva,y_nueva,board):

        direccion = -1 if self.__color__ == "white" else 1

        fila_inicial = 6 if self.__color__ == "white" else 1

        x_actual, y_actual = self.dame_posicion()
        
        if y_nueva == y_actual :
            if x_actual == fila_inicial :
                if self.mover_una_casilla(board,x_nueva,y_nueva,direccion):
                    return True
                elif x_nueva == x_actual + 2 * direccion and board.obtener_pieza(x_actual + direccion,y_actual) is None and board.obtener_pieza(x_nueva,y_nueva) is None :
                    return True
                elif self.mover_una_casilla(board,x_nueva,y_nueva,direccion):
                    return True
        return False

    def mover_una_casilla(self,board,x_nueva,y_nueva,direccion):
        x_actual, y_actual = self.dame_posicion()
        if x_nueva == x_actual + direccion and board.obtener_pieza(x_nueva,y_actual ) is None :
            return True
        return False

    