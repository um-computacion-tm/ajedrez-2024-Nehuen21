class Piece:
    def __init__(self, color,movimiento):
        self.__color__ = color
        self.__movimiento__ = movimiento

    def get_color(self):
        """Devuelve el color de la pieza."""
        return self.__color__

    def get_movimiento(self):
        """Devuelve los posibles movimientos de la pieza."""
        return self.__movimiento__

    def mover(self, nueva_posicion):
        """Mueve la pieza a una nueva posición."""
        # Aquí puedes agregar la lógica para verificar si el movimiento es válido
        # y luego actualizar la posición de la pieza.
        print(f"Moviendo la pieza a la posición {nueva_posicion}")

    def set_color(self, nuevo_color):
        """Cambia el color de la pieza."""
        self.__color__ = nuevo_color