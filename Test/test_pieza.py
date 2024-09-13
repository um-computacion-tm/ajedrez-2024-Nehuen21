import unittest
from game.pieza import Pieza


class TestPieza(unittest.TestCase):

    def setUp(self):                            #Funciona como un input estamos cargando datos hipoteticos
        self.__Pieza__ = Pieza ("blanco",0,0)

    def test_decime_color(self):
        self.assertEqual(self.__Pieza__.decime_color(),"blanco")        #testea que sea el color blanco

    def test_dame_posicion(self):           

        self.assertEqual(self.__Pieza__.dame_posicion(), (0,0))         #testea que este devolviendo bien la posicion

   
    def test_setear_posicion(self):                                         #testea que cambie bien de coordenadas
        x_nueva, y_nueva = 1,1
        self.__Pieza__.setear_posicion(x_nueva, y_nueva)
        self.assertEqual(self.__Pieza__.dame_posicion(),(x_nueva, y_nueva))

    def test_coordenadas_separadas(self):
        x_nueva, y_nueva = 2 , 3
        self.__Pieza__.setear_posicion(x_nueva,y_nueva)
        self.assertEqual(self.__Pieza__.__current_x__,x_nueva)
        self.assertEqual(self.__Pieza__.__current_y__,y_nueva)

    
          
if __name__ == '__main__':
    unittest.main()
