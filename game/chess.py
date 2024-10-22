from game.board import Board
from game.excepciones import PiezaInexistente, MismoColorError, MovimientoInvalido, PosicionError, NoPodesComerAlRey
from game.rey import Rey  

class Ajedrez:
    """Clase principal que gestiona el estado del juego de ajedrez."""

    def __init__(self):
        """Inicializa el tablero y establece el turno inicial en 'BLANCO'."""
        self.__board__ = Board()
        self.__turno_actual__ = "BLANCO"
        self.__board__.setear_piezas()
        self.rey_blanco_capturado = False
        self.rey_negro_capturado = False

    def cambio_de_turno(self):
        """Cambia el turno al otro jugador."""
        self.__turno_actual__ = "NEGRO" if self.__turno_actual__ == "BLANCO" else "BLANCO"

    def turno_actual(self):
        """Devuelve el turno actual.

        """
        return self.__turno_actual__

    def turno_que_sigue(self):
        """Devuelve el turno del siguiente jugador.
        """
        return "NEGRO" if self.__turno_actual__ == "BLANCO" else "BLANCO"

    def estado_del_juego(self):
        """Verifica el estado del juego en función de las piezas restantes."""
        piezas = self.__board__.contar_piezas()
        print(f"Piezas en el tablero: {piezas}")  # Debugging

        if self.rey_blanco_capturado:
            return "Victoria Negra"
        elif self.rey_negro_capturado:
            return "Victoria Blanca"
        elif piezas == [1, 1]:
            return "Empate"

        return "En curso"

    def mostrar_tablero(self):
        """Imprime el estado actual del tablero."""
        print(self.__board__)

    def validar_pieza_turno(self, x, y):
        """Valida que la pieza en la posición dada pertenezca al turno actual.

        
        """
        pieza = self.__board__.obtener_pieza(x, y)

        if pieza is None:
            raise PiezaInexistente(f"No hay ninguna pieza en la posición ({x}, {y}).")

        color_pieza = pieza.decime_color().lower()
        color_turno = self.__turno_actual__.lower()

        if color_pieza != color_turno:
            raise MismoColorError(f"No puedes mover una pieza de color {color_pieza}. Turno actual: {color_turno}")

        return pieza

    def translate_input(self, input_str):
     """Convierte una entrada como 'A1' a coordenadas internas (fila, columna)."""
     if len(input_str) != 2:
         raise PosicionError("La entrada debe tener 2 caracteres, como 'A2'.")

     letter_to_col = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
     letter = input_str[0].upper()
     num = input_str[1]

     if letter not in letter_to_col:
         raise PosicionError(f"Columna '{letter}' inválida. Debe estar entre A y H.")
     col = letter_to_col[letter]

     try:
         row = 8 - int(num)  
         if row < 0 or row > 7:
             raise PosicionError("La fila debe estar entre 1 y 8.")
         return (row, col)
     except ValueError:
         raise PosicionError(f"El segundo carácter '{num}' debe ser un número.")


    def movimientos(self, origen, destino):
     """Gestiona el proceso de mover una pieza en el tablero."""
     try:
         coord_origen = self.translate_input(origen)
         coord_destino = self.translate_input(destino)

         pieza = self.validar_pieza_turno(*coord_origen)

         # Verifica si el destino tiene un rey
         pieza_destino = self.__board__.obtener_pieza(*coord_destino)
         if isinstance(pieza_destino, Rey):
             raise NoPodesComerAlRey("No puedes capturar al rey.")

         # Si no es un rey, procede con la lógica de movimiento
         if self.__board__.mover_pieza(coord_origen, coord_destino):
             estado = self.estado_del_juego()
             if estado == "En curso":
                 self.cambio_de_turno()

             return estado
         else:
             raise MovimientoInvalido("El movimiento no se pudo completar.")

     except (PiezaInexistente, MismoColorError, MovimientoInvalido, NoPodesComerAlRey) as e:
         print(f"\nError: {e}\n")
         raise






        