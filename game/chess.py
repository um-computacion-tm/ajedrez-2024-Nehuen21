from game.board import Board
from game.excepciones import PiezaInexistente,MismoColorError
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
    
    def turno_que_sigue(self):
        if self.__turno_actual__ == "BLANCO":
            return "NEGRO"
        else:
            self.__turn__ = "BLANCO"


    def obtener_pieza_origen(self, x: int, y: int):

        pieza = self.__board__.obtener_pieza(x,y)

        if pieza is None:
            raise PiezaInexistente(f"No existe ninguna pieza en la posicion({x}), ({y}).")
        return pieza
    
    def estado_del_juego(self):
        piezas = self.__board__.contar_piezas()
        print(f"Piezas en el tablero: {piezas}")  # Debugging
        
        if piezas == [1, 1]:
            return "Empate"
        elif piezas[0] == 0:
            return "Victoria Negra"
        elif piezas[1] == 0:
            return "Victoria Blanca"
        
        return "En curso"


    def validaciones(self):
        piezas_vivas = self.__board__.contar_piezas()

        if piezas_vivas[0] == 1 and piezas_vivas[1] == 0:
            return "Victoria Blanca"
        elif piezas_vivas[0] == 0 and piezas_vivas[1] == 1:
            return "Victoria Negra"
        elif piezas_vivas[0] == 1 and piezas_vivas[1] == 1:
            return "Empate"

        return "En curso"
    

    def mostrar_tablero(self):
        print(self.__board__)


    
    def validar_pieza_turno(self, x, y):
         """
         Verifica que la pieza en la posición indicada pertenezca al jugador actual.
         Lanza una excepción si no hay pieza o si la pieza es del color opuesto.
         """
         pieza = self.__board__.obtener_pieza(x, y)

         if pieza is None:
             raise PiezaInexistente(f"No hay ninguna pieza en la posición ({x}, {y}).")

         color_pieza = pieza.decime_color().strip().lower()  # Normalizar color
         color_turno = self.__turno_actual__.strip().lower()  # Normalizar turno

         if color_pieza != color_turno:
             raise MismoColorError(f"No puedes mover una pieza de color {color_pieza}. Turno actual: {color_turno}")

         return pieza