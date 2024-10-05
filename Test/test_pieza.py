import unittest
from game.pieza import Pieza
from game.board import Board

class TestPieza(unittest.TestCase):

    def setUp(self):                            
        self.pieza = Pieza("blanco", 0, 0)   # Inicializamos la pieza
        self.board = Board()  # Inicializamos el tablero
        self.board.setear_piezas()  # Colocamos las piezas en el tablero
        

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

    def test_camino_libre_derecha_horizontal(self):
                                                       # Limpiamos la fila 0 para que no haya piezas en el camino
        self.board._positions[0] = [None] * 8

        # Simulamos un movimiento horizontal de (0, 0) a (0, 7) usando el método de la pieza
        resultado = self.pieza.camino_horizontal_libre(0, 0, 7, self.board)

        # Verificamos que el camino está libre
        self.assertTrue(resultado)

    def test_camino_libre_vertical_arriba(self):
        self.board._positions [1] = [None] * 8

        resultado = self.pieza.camino_vertical_libre(1,1, 7, self.board)

        self.assertTrue(resultado)

    def test_movimiento_horizontal_valido(self):
        # Limpiamos la fila 0 para que no haya piezas en el camino
        self.board._positions[0][0] = [None]  # Aseguramos que no haya piezas en la fila 0
        self.board._positions [1][0] = [None]
        # Colocamos la pieza en la posición inicial
        self.board._positions[0][0] = self.pieza  # Posición (0, 0)

        # Verificamos que el movimiento de (0, 0) a (7, 0) sea válido
        resultado = self.pieza.movimiento_horizontal(0, 0, 1, 0, self.board)
        self.assertTrue(resultado)  # Esto debería pasar si el camino está libre

    def test_movimiento_horizontal_invalido(self):
        # Colocamos una pieza en el camino en la fila 0
        self.board._positions[0][3] = Pieza("negro", 3, 0)

        # Verificamos que el movimiento horizontal no es válido porque hay una pieza en el camino
        resultado = self.pieza.movimiento_horizontal(0, 0, 7, 0, self.board)
        self.assertFalse(resultado)

    def test_movimiento_vertical_invalido(self):
        # Asegúrate de que no haya piezas en la primera y segunda fila de la columna 0
        self.board._positions[0][7] = [None]
        self.board._positions[6][0] = [None]

        # Coloca la pieza en la posición (0, 0)
        self.board._positions[0][7] = self.pieza

        # Realiza la prueba del movimiento vertical
        resultado = self.pieza.movimiento_vertical(0, 7, 6,0 ,  self.board)
        self.assertFalse(resultado)  # Esto debería pasar si el camino está libre


    


    
    

    
if __name__ == '__main__':
    unittest.main()
