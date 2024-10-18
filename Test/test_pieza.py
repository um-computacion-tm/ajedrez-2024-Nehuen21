import unittest
from game.pieza import Pieza
from game.board import Board

class TestPieza(unittest.TestCase):

    def setUp(self):                            
        self.board = Board()  
        self.__pieza__ = Pieza("blanco", 1, 1)
        self.board.setear_tablero(1, 1, self.__pieza__)
    
    def limpiar_posiciones(self, posiciones):
        """Limpia las posiciones indicadas en el tablero."""
        for x, y in posiciones:
            self.board._positions[x][y] = None

    def test_decime_color(self):
        self.assertEqual(self.__pieza__.decime_color(), "blanco")        

    def test_dame_posicion(self):           
        self.assertEqual(self.__pieza__.dame_posicion(), (1, 1))         

    def test_setear_posicion(self):                                         
        x_nueva, y_nueva = 1, 1
        self.__pieza__.setear_posicion(x_nueva, y_nueva)
        self.assertEqual(self.__pieza__.dame_posicion(), (x_nueva, y_nueva))

    def test_coordenadas_separadas(self):
        x_nueva, y_nueva = 2, 3
        self.__pieza__.setear_posicion(x_nueva, y_nueva)
        self.assertEqual(self.__pieza__.__current_x__, x_nueva)
        self.assertEqual(self.__pieza__.__current_y__, y_nueva)

    def test_camino_horizontal_libre_en_fila(self):
     """Valida que no haya obstrucciones en un camino horizontal específico."""
     camino_despejado = self.__pieza__.camino_horizontal_libre(0, 0, 7, self.board)
     self.assertTrue(camino_despejado)
     

    def test_camino_libre_vertical_arriba(self):
        

        resultado = self.__pieza__.camino_vertical_libre(1,1, 7, self.board)

        self.assertTrue(resultado)

  
    


    
    

    
if __name__ == '__main__':
    unittest.main()
