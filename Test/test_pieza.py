import unittest
from game.pieza import Pieza
from game.board import Board


class TestPieza(unittest.TestCase):

    def setUp(self):                            
        self.__Pieza__ = Pieza ("blanco",0,0)
        self.board = Board()  # Inicializamos el tablero
        self.board.setear_piezas()  # Colocamos las piezas en el tablero

    def test_decime_color(self):
        self.assertEqual(self.__Pieza__.decime_color(),"blanco")        

    def test_dame_posicion(self):           

        self.assertEqual(self.__Pieza__.dame_posicion(), (0,0))         

   
    def test_setear_posicion(self):                                        
        x_nueva, y_nueva = 1,1
        self.__Pieza__.setear_posicion(x_nueva, y_nueva)
        self.assertEqual(self.__Pieza__.dame_posicion(),(x_nueva, y_nueva))

    def test_coordenadas_separadas(self):
        x_nueva, y_nueva = 2 , 3
        self.__Pieza__.setear_posicion(x_nueva,y_nueva)
        self.assertEqual(self.__Pieza__.__current_x__,x_nueva)
        self.assertEqual(self.__Pieza__.__current_y__,y_nueva)

    def test_camino_libre_derecha_horizontal(self):
                                                       
        self.board._positions[0] = [None] * 8

        
        resultado = self.__Pieza__.camino_horizontal_libre(0, 0, 7, self.board)
        self.assertTrue(resultado)

    def test_camino_libre_vertical_arriba(self):
        self.board._positions [1] = [None] * 8

        resultado = self.__Pieza__.camino_horizontal_libre(1,1, 7, self.board)

        self.assertTrue(resultado)

    def test_movimiento_horizontal_valido(self):
        # Limpiamos la fila 0 para que no haya piezas en el camino
        self.board._positions[0][0] = [None]  # Aseguramos que no haya piezas en la fila 0
        self.board._positions [1][0] = [None]
        # Colocamos la pieza en la posición inicial
        self.board._positions[0][0] = self.__Pieza__  # Posición (0, 0)

        # Verificamos que el movimiento de (0, 0) a (7, 0) sea válido
        resultado = self.__Pieza__.movimiento_horizontal(0, 0, 1, 0, self.board)
        self.assertTrue(resultado)  # Esto debería pasar si el camino está libre

    def test_movimiento_horizontal_invalido(self):
        # Colocamos una pieza en el camino en la fila 0
        self.board._positions[0][3] = Pieza("negro", 3, 0)

        # Verificamos que el movimiento horizontal no es válido porque hay una pieza en el camino
        resultado = self.__Pieza__.camino_horizontal_libre(0, 0, 7, 0, self.board)
        self.assertFalse(resultado)

    
          
if __name__ == '__main__':
    unittest.main()
