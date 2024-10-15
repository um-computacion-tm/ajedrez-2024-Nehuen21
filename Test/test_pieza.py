import unittest
from game.pieza import Pieza
from game.board import Board

class TestPieza(unittest.TestCase):

    def setUp(self):                            
        self.pieza = Pieza("blanco", 0, 0)   
        self.board = Board()  
        self.board.setear_piezas()  

    def test_decime_color(self):
        self.assertEqual(self.pieza.decime_color(), "blanco")        

    def test_dame_posicion(self):           
        self.assertEqual(self.pieza.dame_posicion(), (0, 0))         

    def test_setear_posicion(self):                                         
        x_nueva, y_nueva = 1, 1
        self.pieza.setear_posicion(x_nueva, y_nueva)
        self.assertEqual(self.pieza.dame_posicion(), (x_nueva, y_nueva))

    def test_coordenadas_separadas(self):
        x_nueva, y_nueva = 2, 3
        self.pieza.setear_posicion(x_nueva, y_nueva)
        self.assertEqual(self.pieza.__current_x__, x_nueva)
        self.assertEqual(self.pieza.__current_y__, y_nueva)

    def test_camino_horizontal_libre_en_fila(self):
     """Valida que no haya obstrucciones en un camino horizontal específico."""
    
     self.board._positions[0] = [None for _ in range(8)]

    
     camino_despejado = self.pieza.camino_horizontal_libre(0, 0, 7, self.board)

     
     self.assertTrue(camino_despejado)


    def test_camino_libre_vertical_arriba(self):
        self.board._positions [1] = [None] * 8

        resultado = self.pieza.camino_vertical_libre(1,1, 7, self.board)

        self.assertTrue(resultado)

    def test_movimiento_horizontal_valido(self):
       
        self.board._positions[0][0] = [None]  
        self.board._positions [0][1] = [None]
     
        self.board._positions[0][0] = self.pieza 

      
        resultado = self.pieza.movimiento_horizontal(0, 0, 0, 1, self.board)
        self.assertTrue(resultado) 

    def test_movimiento_horizontal_invalido(self):
       
        self.board._positions[0][3] = Pieza("negro", 3, 0)

       
        resultado = self.pieza.movimiento_horizontal(0, 0, 7, 0, self.board)
        self.assertFalse(resultado)

    def test_movimiento_vertical_valido(self):
            self.board._positions[1][0] = [None]
            self.board._positions[4][0] = [None]

            self.board._positions[1][0] = self.pieza
            resultado = self.pieza.movimiento_vertical(1, 0, 4, 0, self.board)
            self.assertTrue(resultado)


    def test_movimiento_vertical_invalido(self):
       
        self.board._positions[0][7] = [None]
        self.board._positions[6][0] = [None]

        self.board._positions[0][7] = self.pieza

      
        resultado = self.pieza.movimiento_vertical(0, 7, 6, 0, self.board)
        self.assertFalse(resultado) 

    def test_movimiento_diagonal_valido(self):
        self.board._positions [1] [1] = [None]
        self.board._positions [2] [2] = [None]

        self.board._positions [1][1] = self.pieza

        resultado = self.pieza.movimiento_diagonal(1,1,2,2,self.board)
        self.assertTrue(resultado)

    def test_movimiento_diagonal_invalido(self):
        self.board._positions [0] [7] = [None]
        self.board._positions [6] [0] = [None]

        self.board._positions [0][7] = self.pieza

        resultado = self.pieza.movimiento_diagonal(0, 7, 6,0,self.board)
        self.assertFalse(resultado)

    


    
    

    
if __name__ == '__main__':
    unittest.main()
