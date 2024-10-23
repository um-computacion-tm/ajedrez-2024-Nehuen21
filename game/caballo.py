from game.pieza import Pieza

class Caballo(Pieza):
    def __init__(self,color,x,y):
        super().__init__(color,x,y)

    def __str__(self):
        return "♘" if self.__color__ == "blanco" else "♞"

    def movimiento_valido(self, x_nueva, y_nueva, board):
        delta_x = abs(self.__current_x__ - x_nueva)
        delta_y = abs(self.__current_y__ - y_nueva)

        # El caballo se mueve en forma de "L"
        return (delta_x, delta_y) in [(2, 1), (1, 2)]





