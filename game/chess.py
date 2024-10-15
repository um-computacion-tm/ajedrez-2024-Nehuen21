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