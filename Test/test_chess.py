import unittest

from game.board import Board
from game.chess import Ajedres
from game.torre import Torre
from game.rey import Rey

class TestChess(unittest.TestCase):

    def setUp(self):
        self.__ajedres__=Ajedres()
        self.__board__ = Board()
        


    def testPiezaInexistente(self):
         """Verifica que se lance una excepción si no hay pieza en la posición."""
         with self.assertRaises(Exception):
             self.__ajedres__.obtener_pieza_origen(3,3)

    def test_turno_actual_inicial(self):
        self.assertEqual(self.__ajedres__.turno_actual(),"BLANCO")

    def test_cambio_de_turno(self):
        self.__ajedres__.cambio_de_turno()

        self.assertEqual(self.__ajedres__.turno_actual(),"NEGRO")

        self.__ajedres__.cambio_de_turno()
        self.assertEqual(self.__ajedres__.turno_actual(),"BLANCO")

    
    def test_empate_solo_reyes(self):
     """Verifica que el juego detecte correctamente un empate con solo dos reyes."""
     
     self.__ajedres__.__board__.limpiar_tablero()

    
     self.__rey_blanco__ = Rey("blanco", 0, 4)
     self.__rey_negro__ = Rey("negro", 7, 4)
     self.__ajedres__.__board__.setear_tablero(0, 4, self.__rey_blanco__)
     self.__ajedres__.__board__.setear_tablero(7, 4, self.__rey_negro__)
     piezas = self.__ajedres__.__board__.contar_piezas()
     estado = self.__ajedres__.estado_del_juego()
  
     self.assertEqual(estado, "Empate", "El juego no detectó el empate correctamente.")
    
if __name__ == "__main__":
    unittest.main()
