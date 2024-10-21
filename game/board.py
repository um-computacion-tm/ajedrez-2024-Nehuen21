from game.pieza import Pieza
from game.torre import Torre
from game.alfil import Alfil
from game.reina import Reina
from game.caballo import Caballo
from game.peon import Peon
from game.rey import Rey
from game.excepciones import (
    AjedrezError, MovimientoInvalido, MismoColorError, PiezaInexistente, NoPodesComerAlRey
)

class Board:
    """Clase que representa un tablero de ajedrez y maneja la lógica del juego."""

    def __init__(self):
        """Inicializa el tablero 8x8 con todas las posiciones en `None`."""
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]

    def obtener_pieza(self, x: int, y: int) -> 'Pieza':
        """Obtiene la pieza ubicada en las coordenadas (x, y) del tablero.
        
        Args:
            x (int): Coordenada de fila.
            y (int): Coordenada de columna.

        Returns:
            Pieza | None: La pieza en la posición dada o None si no hay ninguna.
        """
        return self.__positions__[x][y]

    def setear_piezas(self):
        """Coloca las piezas en sus posiciones iniciales en el tablero."""
        self.__positions__[0][0] = Torre("blanco", 0, 0)
        self.__positions__[0][1] = Caballo("blanco", 0, 1)
        self.__positions__[0][2] = Alfil("blanco", 0, 2)
        self.__positions__[0][3] = Reina("blanco", 0, 3)
        self.__positions__[0][4] = Rey("blanco", 0, 4)
        self.__positions__[0][5] = Alfil("blanco", 0, 5)
        self.__positions__[0][6] = Caballo("blanco", 0, 6)
        self.__positions__[0][7] = Torre("blanco", 0, 7)

        for i in range(8):
            self.__positions__[1][i] = Peon("blanco", 1, i)
            self.__positions__[6][i] = Peon("negro", 6, i)

        self.__positions__[7][0] = Torre("negro", 7, 0)
        self.__positions__[7][1] = Caballo("negro", 7, 1)
        self.__positions__[7][2] = Alfil("negro", 7, 2)
        self.__positions__[7][3] = Reina("negro", 7, 3)
        self.__positions__[7][4] = Rey("negro", 7, 4)
        self.__positions__[7][5] = Alfil("negro", 7, 5)
        self.__positions__[7][6] = Caballo("negro", 7, 6)
        self.__positions__[7][7] = Torre("negro", 7, 7)

    def setear_tablero(self, x: int, y: int, pieza: Pieza):
        """Coloca una pieza específica en las coordenadas (x, y).

        Args:
            x (int): Coordenada de fila.
            y (int): Coordenada de columna.
            pieza (Pieza): La pieza a colocar en la posición.
        """
        self.__positions__[x][y] = pieza

    def __str__(self) -> str:
        """Devuelve una representación visual del tablero como una cadena."""
        def crear_linea_etiquetas_columnas():
            return "      a       b       c       d       e       f       g       h\n"

        def crear_linea_superior_inferior(es_inferior=False):
            return (
                "   └───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┘\n"
                if es_inferior else
                "   ┌───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┐\n"
            )

        def crear_linea_separadora():
            return "   ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤\n"

        def crear_fila_con_piezas(fila, numero_fila):
            fila_str = f"  {numero_fila}│"
            for pieza in fila:
                fila_str += f"   {str(pieza) if pieza else ' '}   │"
            return fila_str + f"  {numero_fila}\n"

        tablero = [crear_linea_etiquetas_columnas(), crear_linea_superior_inferior()]
        for i in range(8):
            tablero.append(crear_fila_con_piezas(self.__positions__[i], 8 - i))
            if i < 7:
                tablero.append(crear_linea_separadora())
        tablero.append(crear_linea_superior_inferior(es_inferior=True))
        tablero.append(crear_linea_etiquetas_columnas())
        return "".join(tablero)

    def encontrar_pieza(self, pieza_objetivo: Pieza):
        """Encuentra las coordenadas de una pieza específica en el tablero.

  
        """
        for x in range(8):
            for y in range(8):
                if self.__positions__[x][y] == pieza_objetivo:
                    return (x, y, pieza_objetivo)
        return None

    def obtener_color(self, posicion):
        """Devuelve el color de la pieza en una posición específica.

        """
        x, y = posicion
        pieza = self.obtener_pieza(x, y)
        if not pieza:
            raise PiezaInexistente(f"No hay ninguna pieza en la posición ({x}, {y}).")
        return pieza.decime_color()

    def contar_piezas(self):
        """Cuenta las piezas de cada color en el tablero.

        Returns:
            list[int]: Una lista con dos elementos [blancas, negras].
        """
        contador = [0, 0]
        for fila in self.__positions__:
            for pieza in fila:
                if pieza:
                    contador[0 if pieza.decime_color() == "blanco" else 1] += 1
        return contador

    def mover_pieza(self, origen, destino):
        """Gestiona el movimiento de una pieza de origen a destino.

        
        """
        try:
            self.validar_movimiento(origen, destino)
            self.ejecutar_movimiento(origen, destino)
            return True
        except AjedrezError as e:
            print(f"Error: {str(e)}")
            raise

    def validar_movimiento(self, origen, destino):
        """Valida si el movimiento es permitido.

        Raises:
            PiezaInexistente: Si no hay pieza en la posición de origen.
            NoPodesComerAlRey: Si se intenta capturar al rey.
            MovimientoInvalido: Si el movimiento no es válido para la pieza.
            MismoColorError: Si la posición de destino tiene una pieza del mismo color.
        """
        pieza_origen = self.obtener_pieza(*origen)
        pieza_destino = self.obtener_pieza(*destino)

        if not pieza_origen:
            raise PiezaInexistente("No se encontró ninguna pieza en la posición de origen.")
        if isinstance(pieza_destino, Rey):
            raise NoPodesComerAlRey("No puedes capturar al rey del oponente.")
        if not pieza_origen.movimiento_valido(destino[0], destino[1], self):
            raise MovimientoInvalido("Movimiento inválido para esta pieza.")
        if pieza_destino and pieza_origen.decime_color() == pieza_destino.decime_color():
            raise MismoColorError("No puedes mover a una posición ocupada por otra pieza del mismo color.")

    def limpiar_tablero(self):
        """Limpia el tablero colocando todas las posiciones en `None`."""
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]

    def ejecutar_movimiento(self, origen, destino):
        """Ejecuta el movimiento de una pieza en el tablero."""
        pieza = self.obtener_pieza(*origen)
