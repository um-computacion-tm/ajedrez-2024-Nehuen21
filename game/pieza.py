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