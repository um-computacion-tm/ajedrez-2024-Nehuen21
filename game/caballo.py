from game.pieza import Pieza
class Caballo(Pieza):
    def __init__(self,color,x,y):
        super().__init__(color,x,y)

    def __str__(self):
        return "♘" if self.__color__ == "blanco" else "♞"

    def movimiento_valido(self):
        pass
