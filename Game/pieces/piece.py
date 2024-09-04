class Piece:
    def __init__(self, color,position):
        self.__color__ = color
        self.__position__ = position

    def get_color(self):
        """Devuelve el color de la pieza."""
        return self.__color__

    def get_position(self):
        return self.__position__

    def check_position(self,new_position):           #Nueva posicion
        self.__position__ = new_position

    def __str__(self):
        return " "
    
    def check_move(self,positions,new_positions):
        return True
    
    def obtener_coordenadas(self,positions,new_positions):
        x,y = new_positions

    @property
    def get_color(self) -> str:
        return self.__color__
        

    
    

