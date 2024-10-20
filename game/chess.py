from game.board import Board
from game.excepciones import AjedrezError,PiezaInexistente
class Ajedres:
    def __init__(self):
        self.__board__ = Board()
        self.__turno_actual__ = "BLANCO"

    def cambio_de_turno(self):
        if self.__turno_actual__ == "BLANCO":
            self.__turno_actual__ = "NEGRO"
        else:
            self.__turno_actual__ = "BLANCO"

    def turno_actual(self):
        return self.__turno_actual__
    
    def obtener_pieza_origen(self, x: int, y: int):

        pieza = self.__board__.obtener_pieza(x,y)

        if pieza is None:
            raise PiezaInexistente(f"No existe ninguna pieza en la posicion({x}), ({y}).")
        return pieza
    
    def validaciones(self, movimiento_exitoso):
        if not movimiento_exitoso:
            return False  

        estado = self.estado_del_juego()

        if estado == "Empate":
            return "Empate"
        elif estado == "Victoria Blanca":
            return "Victoria Blanca"
        elif estado == "Victoria Negra":
            return "Victoria Negra"

      
        self.cambio_de_turno()
        return True 


    def estado_del_juego(self):
        lista = self.__board__.contar_piezas()

        if lista == (1,1) :
            return "Empate" 

        elif lista == (1,0) :
            return "Victoria Blanca"  

        elif lista== (0,1):
            return "Victoria Negra" 

        return 