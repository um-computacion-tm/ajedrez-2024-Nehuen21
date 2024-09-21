from game.torre import Torre
from game.king import King
from game.pawn import Pawn
from game.queen import Queen
from game.bishoop import Bishoop
from game.knight import Knight
from game.pieza import Pieza

class Board:
    def __init__(self,positions):

        self._positions = []
        for _ in range(8):
            col = []
        for i in range(8):
            col.append(None)

        self.__positions__.append(col)

    def obtener_pieza(self,row,col):
        return self.__positions__ [row],[col]

    def setear_piezas(self):
        self.__positions__ [0,0] = Torre("white",(0,0))
        self.__positions__ [0,1] = Knight("white", (0,1))
        self.__positions__ [0,2] = Bishoop("white",(0,2))               
        self.__positions__ [0,3] = Queen("white",(0,3))       
        self.__positions__ [0,4] = King("white",(0,4))
        self.__positions__ [0,5] = Bishoop("white",(0,5))       
        self.__positions__ [0,6] = Knight("white",(0,6))       
        self.__positions__ [0,7] = Torre("White",(0,7))

        for i in range (8):
            self.__positions__ = Pawn ("white", (1,i))
            self.__positions__ = Pawn("black", (6,i))

        self.__positions__ [7,0] = Torre("black",(7,0))
        self.__positions__ [7,1] = Knight("black", (7,1))
        self.__positions__ [7,2] = Bishoop("black",(7,2))               
        self.__positions__ [7,3] = Queen("black",(7,3))       
        self.__positions__ [7,4] = King("black",(7,4))
        self.__positions__ [7,5] = Bishoop("black",(7,5))       
        self.__positions__ [7,6] = Knight("black",(7,6))       
        self.__positions__ [7,7] = Torre("black",(7,7))

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

        




        