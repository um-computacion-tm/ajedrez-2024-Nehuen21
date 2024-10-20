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
        # Limpiar el tablero antes de comenzar
        self.__board__.limpiar_tablero()

        # Colocar solo los dos reyes
        self.__board__.setear_tablero(0, 4, Rey("blanco", 0, 4))
        self.__board__.setear_tablero(7, 4, Rey("negro", 7, 4))

        # Confirmar el estado del juego
        estado = self.__ajedres__.estado_del_juego()
        print(self.__board__)
        self.assertEqual(self.__ajedres__.estado_del_juego(), "Empate")
    
if __name__ == "__main__":
    unittest.main()
