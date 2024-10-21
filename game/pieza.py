class Pieza:
    """Clase base que representa una pieza genérica de ajedrez."""

    def __init__(self, color, x, y):
        """Inicializa una pieza con su color y posición en el tablero.

        Args:
            color (str): Color de la pieza ('blanco' o 'negro').
            x (int): Coordenada inicial en el eje X (fila).
            y (int): Coordenada inicial en el eje Y (columna).
        """
        self.__color__ = color
        self.__current_x__ = x
        self.__current_y__ = y

    def decime_color(self):
        """Devuelve el color de la pieza.

        Returns:
            str: El color de la pieza ('blanco' o 'negro').
        """
        return self.__color__

    def dame_posicion(self):
        """Devuelve la posición actual de la pieza en el tablero.

        Returns:
            tuple[int, int]: Coordenadas (x, y) de la pieza.
        """
        return self.__current_x__, self.__current_y__

    def setear_posicion(self, x_nueva, y_nueva):
        """Actualiza la posición de la pieza en el tablero.

        Args:
            x_nueva (int): Nueva coordenada en el eje X (fila).
            y_nueva (int): Nueva coordenada en el eje Y (columna).
        """
        self.__current_x__ = x_nueva
        self.__current_y__ = y_nueva

    def __str__(self):
        """Devuelve una representación en cadena de la pieza. 
        Debe ser sobreescrito por las clases hijas.

        Returns:
            str: Representación de la pieza.
        """
        return ""

    def camino_libre(self, coord_inicial, coord_final, constante, es_horizontal, board):
        """Verifica si el camino entre dos coordenadas está libre de otras piezas.

        

        Returns:
            bool: True si el camino está libre, False en caso contrario.
        """
        rango = (
            range(coord_inicial + 1, coord_final)
            if coord_inicial < coord_final
            else range(coord_final + 1, coord_inicial)
        )

        for i in rango:
            pieza = (
                board.obtener_pieza(i, constante) if es_horizontal 
                else board.obtener_pieza(constante, i)
            )
            if pieza is not None:
                return False

        return True

    def camino_horizontal_libre(self, x, y, x_nueva, board):
        """Verifica si el camino horizontal está libre de piezas.

        

        Returns:
            bool: True si el camino está libre, False en caso contrario.
        """
        return self.camino_libre(x, x_nueva, y, es_horizontal=True, board=board)

    def camino_vertical_libre(self, x, y, y_nueva, board):
        """Verifica si el camino vertical está libre de piezas.

       

        Returns:
            bool: True si el camino está libre, False en caso contrario.
        """
        return self.camino_libre(y, y_nueva, x, es_horizontal=False, board=board)

    def movimiento_vertical(self, x, y, x_nueva, y_nueva, board):
        """Valida un movimiento vertical de la pieza.

       

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        if y != y_nueva or x == x_nueva:
            return False

        paso_h = 1 if x_nueva > x else -1
        for i in range(1, abs(x_nueva - x)):
            if board.obtener_pieza(x + i * paso_h, y) is not None:
                return False

        return True

    def movimiento_horizontal(self, x, y, x_nueva, y_nueva, board):
        """Valida un movimiento horizontal de la pieza.

        
        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        if x != x_nueva or y == y_nueva:
            return False

        paso_v = 1 if y_nueva > y else -1
        for i in range(1, abs(y_nueva - y)):
            if board.obtener_pieza(x, y + i * paso_v) is not None:
                return False

        return True

    def movimiento_diagonal(self, x, y, x_nueva, y_nueva, board):
        """Valida un movimiento diagonal de la pieza.

        

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        if abs(x_nueva - x) != abs(y_nueva - y):
            return False

        paso_x = 1 if x_nueva > x else -1
        paso_y = 1 if y_nueva > y else -1

        for i in range(1, abs(x_nueva - x)):
            if board.obtener_pieza(x + i * paso_x, y + i * paso_y) is not None:
                return False

        return True
