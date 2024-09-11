from game.pieza import Pieza

import unittest

class TestPieza(unittest.TestCase):
    
    def setUp(self):
        
        self.__Pieza__ = Pieza ("blanco",(0,0))

    def test_decime_color(self):
        self.assertEqual(self.__Pieza__.decime_color(),"blanco")

    def test_dame_posicion(self):

        self.assertEqual(self.__Pieza__.dame_posicion(),(0,0))

   
    def test_setear_posicion(self):
        nueva_posicion = (1,1)
        self.__Pieza__.setear_posicion(nueva_posicion)
        self.assertEqual(self.__Pieza__.dame_posicion,nueva_posicion(1,1))

    

   
if __name__ == '__main__':
    unittest.main()
