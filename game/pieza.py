
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
    
    
    def camino_libre(self, coord_inicial, coord_final, constante, es_horizontal, board):

        if coord_inicial < coord_final:
            rango = range(coord_inicial + 1, coord_final)
        else:
            rango = range(coord_final + 1, coord_inicial)

        for i in rango:
            if es_horizontal:
                pieza = board.obtener_pieza(i, constante)  # Horizontal: variamos x
            else:
                pieza = board.obtener_pieza(constante, i)  # Vertical: variamos y

            if pieza is not None:
                return False

        return True


    def camino_horizontal_libre(self, x, y, x_nueva, board):
       
        return self.camino_libre(x, x_nueva, y, es_horizontal=True, board=board)

    def camino_vertical_libre(self, x, y, y_nueva, board):
        return self.camino_libre(y, y_nueva, x, es_horizontal=False, board=board)

    
    def movimiento_horizontal(self, x, y, x_nueva, y_nueva, board):
        if x != x_nueva or y == y_nueva:  
            return False

        paso_v = 1 if y_nueva > y else -1

        for i in range(1, abs(y_nueva - y)):
            if board.obtener_pieza(x, y + i * paso_v) is not None:
                return False

        return True
    def movimiento_vertical(self, x, y, x_nueva, y_nueva, board):
        
        if y != y_nueva or x == x_nueva:  
            return False
        paso_h = 1 if x_nueva > x else -1

        for i in range(1, abs(x_nueva - x)):
            if board.obtener_pieza(x + i * paso_h, y) is not None:
                return False  

        
        return True  

    def movimiento_diagonal(self, x, y, x_nueva, y_nueva, board):
       
        if abs(x_nueva - x) != abs(y_nueva - y):
            return False

        paso_y = 1 if y_nueva > y else -1 
        paso_x = 1 if x_nueva > x else -1

        for i in range(1, abs(x_nueva - x)):
            if board.obtener_pieza(x + i * paso_x, y + i * paso_y) is not None:
                return False
        return True
        

 
        


        







