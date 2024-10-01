#Check
class Pieza:

    def __init__(self,color,x,y):
        self.__color__ = color
        self.__current_x__ =  x
        self.__current_y__ =  y

    def decime_color(self):
        return self.__color__
    
    def dame_posicion(self):
        return self.__current_x__, self.__current_y__
    
    def setear_posicion(self,x_nueva,y_nueva):
         self.__current_x__ = x_nueva
         self.__current_y__ = y_nueva

    def __str__(self) :
        return ""
    
    def camino_horizontal_libre(self, x, y, x_nueva, board):
        """Verifica si el camino horizontal está libre en el tablero"""

        if x < x_nueva:  # Movimiento hacia la derecha
            for columna in range(x + 1, x_nueva):
                if board.obtener_pieza(y, columna) is not None:
                    return False
        else:  # Movimiento hacia la izquierda
            for columna in range(x_nueva + 1, x):
                if board.obtener_pieza(y, columna) is not None:
                    return False
        return True
    
    def camino_vertical_libre(self,x,y,y_nueva,board):
        if y < y_nueva :                                       
            for fila in range(y + 1, y_nueva):
                if board.obtener_pieza(x,fila) is not None:
                    return False
        else:
            for fila in range(y_nueva + 1, y ):                     
                if board.obtener_pieza(x,fila) is not None:
                    return False
        return True