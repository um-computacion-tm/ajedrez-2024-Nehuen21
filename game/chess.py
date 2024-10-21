from game.board import Board
from game.excepciones import PiezaInexistente,MismoColorError,MovimientoInvalido,PosicionError
class Ajedrez:
    def __init__(self):
        self.__board__ = Board()
        self.__turno_actual__ = "BLANCO"
        self.__board__.setear_piezas()

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
            return "BLANCO"


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
        pieza = self.__board__.obtener_pieza(x, y)

        if pieza is None:
            raise PiezaInexistente(f"No hay ninguna pieza en la posición ({x}, {y}).")

        color_pieza = pieza.decime_color().strip().lower()
        color_turno = self.__turno_actual__.strip().lower()

        if color_pieza != color_turno:
            raise MismoColorError(f"No puedes mover una pieza de color {color_pieza}. Turno actual: {color_turno}")

        return pieza


    

    
    def translate_input(self, input_str):
        """
        Transforma una entrada como 'A2' a las coordenadas internas (fila, columna).
        """
        if len(input_str) != 2:
            raise PosicionError("La entrada debe tener exactamente 2 caracteres, como 'A2'.")

        
        letter_to_col = {
            'A': 0, 'B': 1, 'C': 2, 'D': 3,
            'E': 4, 'F': 5, 'G': 6, 'H': 7
        }

        
        letter = input_str[0].upper()
        num = input_str[1]

        
        if letter not in letter_to_col:
            raise PosicionError(f"La columna '{letter}' es inválida. Debe estar entre A y H.")
        col = letter_to_col[letter]

        
        try:
            row = int(num)
            if row < 1 or row > 8:
                raise PosicionError("La fila debe estar entre 1 y 8.")

            
            
            return (row, col)

        except ValueError:
            raise PosicionError(f"El segundo carácter '{num}' debe ser un número.")






    def movimientos(self, origen, destino):
        try:
           
            coord_origen = self.translate_input(origen)
            coord_destino = self.translate_input(destino)

           
            self.pieza = self.validar_pieza_turno(*coord_origen)

            
            if self.__board__.mover_pieza(coord_origen, coord_destino):
                estado = self.estado_del_juego()  

                
                if estado == "En curso":
                    self.cambio_de_turno()

                return estado
            else:
                raise MovimientoInvalido("El movimiento no se pudo completar.")
        except (PiezaInexistente, MismoColorError, MovimientoInvalido) as e:
            raise e

    



