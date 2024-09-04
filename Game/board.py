from pieces.rook import Rook
from pieces.king import King
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.bishoop import Bishoop
from pieces.knight import Knight

class Board:
    def __init__(self):

        self._positions = []
        for _ in range(8):
            col = []
        for i in range(8):
            col.append(None)

        self.__positions__.append(col)

    def obtener_pieza(self,row,col):
        return self.__positions__ [row],[col]

    def setear_piezas(self):
        self.__positions__ [0,0] = Rook("White",(0,0))
        self.__positions__ [1,0] = Knight("White", (1,0))
        self.__positions__ [2,0] = Bishoop("Bishop",(2,0))               
        self.__positions__ [3,0] = Queen("Queen",(3,0))       
        self.__positions__ [4,0] = King("King",(4,0))
        self.__positions__ [3,0] = Bishoop("",(5,0))       
        self.__positions__ [4,0] = Knight("Knight",(6,0))       
        self.__positions__ [7,0] = Rook("White",(7,0))

        