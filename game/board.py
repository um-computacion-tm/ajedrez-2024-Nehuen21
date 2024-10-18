from game.pieza import Pieza
from game.torre import Torre
from game.alfil import Alfil
from game.reina import Reina
from game.caballo import Caballo
from game.peon import Peon
from game.rey import Rey
from game.excepciones import AjedrezError, MovimientoInvalido, MovimientoErrorPieza,MismoColorError,PiezaInexistente,NoPodesComerAlRey,PosicionError
class Board:
    
    def __init__(self):
        # Inicializa el tablero 8x8 con None
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]

    def obtener_pieza(self, x: int, y: int) -> 'Pieza': 
            return self.__positions__[x][y]



    def setear_piezas(self):
        """Coloca las piezas en sus posiciones iniciales."""
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

    def setear_tablero(self,x,y,pieza):
        self.__positions__[x][y] = pieza

    def __str__(self):
        def crear_linea_etiquetas_columnas():
            columnas = [chr(i) for i in range(ord('a'), ord('h') + 1)]
            return "      a       b       c       d       e       f       g       h\n"

        def crear_linea_superior_inferior(es_inferior=False):
            if es_inferior:
                return "   └───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┘\n"
            return "   ┌───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┐\n"

        def crear_linea_separadora():
            return "   ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤\n"

        def crear_fila_con_piezas(fila, numero_fila):
            fila_str = f"  {numero_fila}│"
            for pieza in fila:
                if pieza is None:
                    fila_str += "       │"
                else:
                    fila_str += f"   {str(pieza)}   │"
            return fila_str + f"  {numero_fila}\n"

        # Construcción del tablero
        tablero = []
        tablero.append(crear_linea_etiquetas_columnas())    
        tablero.append(crear_linea_superior_inferior())

        for fila_index in range(8):
            fila_actual = self.__positions__[fila_index]
            tablero.append(crear_fila_con_piezas(fila_actual, 8 - fila_index))
            if fila_index != 7:
                tablero.append(crear_linea_separadora())

        tablero.append(crear_linea_superior_inferior(es_inferior=True))
        tablero.append(crear_linea_etiquetas_columnas())

        return "".join(tablero)
    
    def obtener_color(self, posicion):
        """Obtiene el color de la pieza en una posición específica del tablero."""
        x, y = posicion  

        pieza = self.obtener_pieza(x, y)  

        if not pieza:  
            raise PiezaInexistente(f"No hay ninguna pieza en la posición ({x}, {y}).")

        return pieza.decime_color()


    def contar_piezas(self):
        """Cuenta cuántas piezas hay de cada color en el tablero."""
        contador = {"blanco": 0, "negro": 0}

        for fila in self.__positions__:
            for pieza in fila:
                if pieza is not None:
                    color = pieza.decime_color()
                    if color in contador:
                        contador[color] += 1

        return contador
    
    def limpiar_tablero(self):
        """Limpia el tablero estableciendo todas las posiciones en None."""
        for x in range(8):
            for y in range(8):
                self.__positions__[x][y] = None
    


    def encontrar_pieza(self, pieza_objetivo):
        """Encuentra la posición de una pieza específica en el tablero."""
        for x in range(8):
            for y in range(8):
                pieza = self.__positions__[x][y]
                if pieza == pieza_objetivo:
                    return (x, y, pieza)
        return None 

    
    def mover_pieza(self, origen, destino):
        """Gestiona el movimiento de una pieza de origen a destino."""
        try:
            self.validar_movimiento(origen, destino)  
            self.ejecutar_movimiento(origen, destino)  
            return True 
        except AjedrezError as e:
            print(f"Error: {str(e)}")
            raise  

    def validar_movimiento(self, origen, destino):
        """Valida que el movimiento de la pieza sea permitido."""
        pieza_origen = self.obtener_pieza(*origen)
        pieza_destino = self.obtener_pieza(*destino)

        if pieza_origen is None:
            raise PiezaInexistente("No se encontró ninguna pieza en la posición de origen.")

        if isinstance(pieza_destino, Rey):
            raise NoPodesComerAlRey("No puedes capturar al rey del oponente.")

        if not pieza_origen.movimiento_valido(destino[0], destino[1], self):
            raise MovimientoInvalido("Movimiento inválido para esta pieza.")

        if pieza_destino and pieza_origen.decime_color() == pieza_destino.decime_color():
            raise MismoColorError("No puedes mover la pieza a una posición ocupada por otra del mismo color.")


    def ejecutar_movimiento(self, origen, destino):
   
     pieza_origen = self.obtener_pieza(*origen)

     self.setear_tablero(destino[0], destino[1], pieza_origen)
     self.setear_tablero(origen[0], origen[1], None)
     pieza_origen.setear_posicion(*destino)




if __name__ == '__main__':

    tablero = Board()
    tablero.setear_piezas()
    print(tablero)

    




    
