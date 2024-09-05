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
        self.__positions__ [0,0] = Rook("white",(0,0))
        self.__positions__ [0,1] = Knight("white", (0,1))
        self.__positions__ [0,2] = Bishoop("white",(0,2))               
        self.__positions__ [0,3] = Queen("white",(0,3))       
        self.__positions__ [0,4] = King("white",(0,4))
        self.__positions__ [0,5] = Bishoop("white",(0,5))       
        self.__positions__ [0,6] = Knight("white",(0,6))       
        self.__positions__ [0,7] = Rook("White",(0,7))

        for i in range (8):
            self.__positions__ = Pawn ("white", (1,i))
            self.__positions__ = Pawn("black", (6,i))

        self.__positions__ [7,0] = Rook("black",(7,0))
        self.__positions__ [7,1] = Knight("black", (7,1))
        self.__positions__ [7,2] = Bishoop("black",(7,2))               
        self.__positions__ [7,3] = Queen("black",(7,3))       
        self.__positions__ [7,4] = King("black",(7,4))
        self.__positions__ [7,5] = Bishoop("black",(7,5))       
        self.__positions__ [7,6] = Knight("black",(7,6))       
        self.__positions__ [7,7] = Rook("black",(7,7))



        