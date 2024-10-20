from game.board import Board
from game.excepciones import PiezaInexistente,MismoColorError,MovimientoInvalido
class Ajedrez:
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
         """
         Verifica que la pieza en la posición indicada pertenezca al jugador actual.
         Lanza una excepción si no hay pieza o si la pieza es del color opuesto.
         """
         pieza = self.__board__.obtener_pieza(x, y)

         if pieza is None:
             raise PiezaInexistente(f"No hay ninguna pieza en la posición ({x}, {y}).")

         color_pieza = pieza.decime_color().strip().lower()  # Normalizar color
         color_turno = self.__turno_actual__.strip().lower()  # Normalizar turno

         if color_pieza != color_turno:
             raise MismoColorError(f"No puedes mover una pieza de color {color_pieza}. Turno actual: {color_turno}")

         return pieza
    
    def traducir_input(self, entrada):
        """
        Convierte una entrada alfanumérica, como 'C3', a una tupla de coordenadas internas del tablero.
        """
        if len(entrada) != 2:
            raise ValueError("La entrada debe tener dos caracteres: una letra y un número.")

        columna = entrada[0].lower()  
        fila = entrada[1]

        if columna < 'a' or columna > 'h' or not fila.isdigit():
            raise ValueError("Entrada inválida. Debe estar en el rango A1-H8.")


        indice_columna = ord(columna) - ord('a')


        indice_fila = int(fila) - 1

        if indice_fila < 0 or indice_fila > 7 or indice_columna < 0 or indice_columna > 7:
            raise ValueError("La entrada está fuera del rango del tablero.")

        return (indice_fila, indice_columna)
    
    def movimientos(self, origen, destino):
        """
        Gestiona el proceso completo de mover una pieza:
        - Convierte las entradas del usuario a coordenadas.
        - Verifica que la pieza seleccionada sea del jugador actual.
        - Intenta realizar el movimiento y verifica el estado del juego.
        - Gestiona las excepciones relacionadas con movimientos inválidos.
        """
        try:
           
            coord_origen = self.traducir_input(origen)
            coord_destino = self.traducir_input(destino)

            pieza = self.validar_pieza_turno(*coord_origen)
            movimiento_exitoso = self.__board__.mover_pieza(coord_origen, coord_destino)

            
            if movimiento_exitoso:
                estado = self.estado_del_juego()

               
                if estado == "En curso":
                    self.cambio_de_turno()

                
                return estado
            else:
                raise MovimientoInvalido("El movimiento no se pudo completar.")

        except PiezaInexistente as e:
            raise e  
        except MismoColorError as e:
            raise e  
        except MovimientoInvalido as e:
            raise e  
