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
    
    def test_victoria_negra(self):
     """Verifica que el juego detecte correctamente una victoria negra."""
    
     self.__ajedres__.__board__.limpiar_tablero()

     
     rey_negro = Rey("negro", 7, 4)
     torre_negra = Torre("negro", 6, 4)

     self.__ajedres__.__board__.setear_tablero(7, 4, rey_negro)
     self.__ajedres__.__board__.setear_tablero(6, 4, torre_negra)

     
     estado = self.__ajedres__.estado_del_juego()

    
     self.assertEqual(estado, "Victoria Negra", "El juego no detectó la victoria negra correctamente.")

    def test_victoria_blanca(self):
        """Verifica que el juego detecte correctamente una victoria blanca."""
        
        self.__ajedres__.__board__.limpiar_tablero()

       
        rey_blanco = Rey("blanco", 0, 4)
        torre_blanca = Torre("blanco", 1, 4)

        self.__ajedres__.__board__.setear_tablero(0, 4, rey_blanco)
        self.__ajedres__.__board__.setear_tablero(1, 4, torre_blanca)

   
        estado = self.__ajedres__.estado_del_juego()

       
        self.assertEqual(estado, "Victoria Blanca", "El juego no detectó la victoria blanca correctamente.")
if __name__ == "__main__":
    unittest.main()
