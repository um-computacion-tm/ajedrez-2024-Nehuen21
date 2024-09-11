class Pieza:
    def __init__(self, color,posicion):
        self.__color__ = color
        self.__posicion__ = posicion

    def decime_color(self):
        
        return self.__color__

    def dame_posicion(self):
        return self.__posicion__

    def setear_posicion(self,posicion_nueva):           #Nueva posicion
        self.__posicion__ = posicion_nueva

    def __str__(self):
        return " "
    
    def check_movimiento(self,posicion,posicion_nueva):
        return True
    
    def obtener_coordenadas(self,posicion_nueva):
        x,y = posicion_nueva
        x_actual , y_actual = self.__posicion__
        return x,y, x_actual,y_actual

    @property
    def get_color(self) -> str:
        return self.__color__
        

    
    

