from game.pieza import Pieza

class Peon(Pieza):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def __str__(self):
        return "♙" if self.__color__ == "blanco" else "♟"

    def movimiento_valido(self, x_nueva, y_nueva, board):
        """Valida un movimiento de peón.
    
        Args:
            x_nueva (int): Nueva coordenada en el eje X.
            y_nueva (int): Nueva coordenada en el eje Y.
            board (Board): Instancia del tablero.
    
        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        x_actual, y_actual = self.dame_posicion()
        # Determinar dirección de movimiento basada en el color
        direccion = 1 if self.decime_color() == "blanco" else -1
        fila_inicial = 1 if self.decime_color() == "blanco" else 6  # Filas de inicio de los peones
    
        # Movimiento hacia adelante
        if x_nueva == x_actual + direccion and y_nueva == y_actual:
            return board.obtener_pieza(x_nueva, y_nueva) is None  # Movimiento simple
    
        # Doble movimiento
        if x_actual == fila_inicial and x_nueva == x_actual + 2 * direccion and y_nueva == y_actual:
            return (board.obtener_pieza(x_actual + direccion, y_actual) is None and 
                    board.obtener_pieza(x_nueva, y_nueva) is None)  # Ambas casillas deben estar vacías
    
        # Captura diagonal
        if x_nueva == x_actual + direccion and abs(y_nueva - y_actual) == 1:
            return board.obtener_pieza(x_nueva, y_nueva) is not None  # Debe haber una pieza del color opuesto
    
        return False  # Movimiento inválido
    
    