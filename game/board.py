from game.pieza import Pieza
from game.torre import Torre
from game.alfil import Alfil
from game.reina import Reina
from game.caballo import Caballo
from game.peon import Peon
from game.rey import Rey

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
    
    def camino_horizontal_libre(self, x, y, x_nueva, board):
       

        if x < x_nueva:  
            for columna in range(x + 1, x_nueva):
                if board.obtener_pieza(y, columna) is not None:
                    return False
        else:  
            for columna in range(x_nueva + 1, x):
                if board.obtener_pieza(y, columna) is not None:
                    return False
        return True
    
    def camino_vertical_libre(self, x, y, y_nueva, board):
        if y < y_nueva: 
            for fila in range(y + 1, y_nueva):
                if board.obtener_pieza(x, fila) is not None:
                    return False
        else:  
            for fila in range(y_nueva + 1, y):
                if board.obtener_pieza(x, fila) is not None:
                    return False
        return True

        
    def encontrar_pieza(self, pieza_objetivo):
        """Encuentra la posición de una pieza específica en el tablero."""
        for x in range(8):
            for y in range(8):
                pieza = self.__positions__[x][y]
                if pieza == pieza_objetivo:
                    return (x, y, pieza)
        return None 



if __name__ == '__main__':

    tablero = Board()
    tablero.setear_piezas()
    print(tablero)

    




    
