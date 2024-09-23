#Check
from game.torre import Torre
from game.alfil import Alfil
from game.reina import Reina
from game.caballo import Caballo
from game.peon import Peon
from game.rey import Rey

class Board:
    
    def __init__(self):
        # Inicializa el tablero 8x8 con None
        self._positions = [[None for _ in range(8)] for _ in range(8)]

    def obtener_pieza(self, fila, columna):
        """Obtiene la pieza en una posición dada."""
        return self._positions[fila][columna]

    def setear_piezas(self):
        """Coloca las piezas en sus posiciones iniciales."""
        self._positions[0][0] = Torre("blanco", 0, 0)
        self._positions[0][1] = Caballo("blanco", 0, 1)
        self._positions[0][2] = Alfil("blanco", 0, 2)               
        self._positions[0][3] = Reina("blanco", 0, 3)       
        self._positions[0][4] = Rey("blanco", 0, 4)
        self._positions[0][5] = Alfil("blanco", 0, 5)       
        self._positions[0][6] = Caballo("blanco", 0, 6)       
        self._positions[0][7] = Torre("blanco", 0, 7)

        for i in range(8):
            self._positions[1][i] = Peon("blanco", 1, i)
            self._positions[6][i] = Peon("negro", 6, i)

        self._positions[7][0] = Torre("negro", 7, 0)
        self._positions[7][1] = Caballo("negro", 7, 1)
        self._positions[7][2] = Alfil("negro", 7, 2)               
        self._positions[7][3] = Reina("negro", 7, 3)       
        self._positions[7][4] = Rey("negro", 7, 4)
        self._positions[7][5] = Alfil("negro", 7, 5)       
        self._positions[7][6] = Caballo("negro", 7, 6)       
        self._positions[7][7] = Torre("negro", 7, 7)

    def __str__ (self):
         def crear_linea_etiquetas_columnas():
            columnas = [chr(i) for i in range(ord('a'), ord('h') + 1)]
            return "    " + "   ".join(columnas) + "\n"
        
         def crear_linea_superior_inferior(es_inferior=False):
            if es_inferior:
                return "  " + "└" + "───┴" * 7 + "───┘" + "\n"
            return "  " + "┌" + "───┬" * 7 + "───┐" + "\n"

         def crear_linea_separadora():
            return "  " + "├" + "───┼" * 7 + "───┤" + "\n"

         def crear_fila_con_piezas(fila, numero_fila):
            fila_str = f" {numero_fila} │"
            for pieza in fila:
                if pieza is None:
                    fila_str += "   │"
                else:
                    fila_str += f" {str(pieza)} │"
            return fila_str + f" {numero_fila}\n"

        # Construcción del tablero
         tablero = []
         tablero.append(crear_linea_etiquetas_columnas())
         tablero.append(crear_linea_superior_inferior())

         for fila_index in range(8):
            fila_actual = self._positions[fila_index]
            tablero.append(crear_fila_con_piezas(fila_actual, 8 - fila_index))
            if fila_index != 7:
                tablero.append(crear_linea_separadora())

         tablero.append(crear_linea_superior_inferior(es_inferior=True))
         tablero.append(crear_linea_etiquetas_columnas())

         return "".join(tablero)
    

if __name__ == '__main__':

    tablero = Board()
    tablero.setear_piezas()
    print(tablero)

    




    
