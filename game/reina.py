from game.pieza import Pieza

class Reina(Pieza):
    def __init__(self,color,x,y):
        super().__init__(color,x,y)

    def __str__(self):
        return "♕" if self.__color__ == "blanco" else "♛"
    
    def movimiento_valido(self,x_nueva,y_nueva,board):
         if self.movimiento_diagonal(self.__current_x__, self.__current_y__,x_nueva,y_nueva,board) :
             return True
         elif self.movimiento_horizontal(self.__current_x__, self.__current_y__,x_nueva,y_nueva,board) : 
             return True
         elif self.movimiento_vertical(self.__current_x__, self.__current_y__,x_nueva,y_nueva,board) :
             return True
         else :
             return False