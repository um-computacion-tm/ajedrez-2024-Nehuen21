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

    def test_movimiento_horizontal_valido(self):
       
        
        resultado = self.__pieza__.movimiento_horizontal(0, 0, 0, 1, self.board)
        self.assertTrue(resultado)

    def test_movimiento_horizontal_invalido(self):
       
        self.board._positions[0][3] = Pieza("negro", 3, 0)

       
        resultado = self.__pieza__.movimiento_horizontal(0, 0, 7, 0, self.board)
        self.assertFalse(resultado)

    def test_movimiento_vertical_valido(self):
        
        resultado_aceptado = self.__pieza__.movimiento_vertical(1, 0, 4, 0, self.board)
        self.assertTrue(resultado_aceptado)


    def test_movimiento_vertical_invalido(self):
       
        
        resultado_erroneo = self.__pieza__.movimiento_diagonal(0, 7, 6, 0, self.board)
        self.assertFalse(resultado_erroneo) 

    def test_movimiento_diagonal_valido(self):
        
        salida_valida = self.__pieza__.movimiento_diagonal(1, 1, 2, 2, self.board)
        self.assertTrue(salida_valida)

    def test_movimiento_diagonal_invalido(self):
        
        salida_invalida = self.__pieza__.movimiento_diagonal(0, 7, 6, 0, self.board)
        self.assertFalse(salida_invalida)

    


    
    

    
if __name__ == '__main__':
    unittest.main()
