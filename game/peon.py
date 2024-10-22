from game.pieza import Pieza

class Peon(Pieza):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def __str__(self):
        return "♙" if self.__color__ == "blanco" else "♟"

    def movimiento_valido(self, x_nueva, y_nueva, board):
        """Valida un movimiento de peón.

        """
        x_actual, y_actual = self.dame_posicion()

        # Movimiento hacia adelante
        if self.decime_color() == "blanco":
            if x_nueva == x_actual + 1 and y_nueva == y_actual:
                return board.obtener_pieza(x_nueva, y_nueva) is None  # Movimiento simple
            elif x_nueva == x_actual + 1 and abs(y_nueva - y_actual) == 1:
                return board.obtener_pieza(x_nueva, y_nueva) is not None  # Captura

        elif self.decime_color() == "negro":
            if x_nueva == x_actual - 1 and y_nueva == y_actual:
                return board.obtener_pieza(x_nueva, y_nueva) is None  # Movimiento simple
            elif x_nueva == x_actual - 1 and abs(y_nueva - y_actual) == 1:
                return board.obtener_pieza(x_nueva, y_nueva) is not None  # Captura

        return False
