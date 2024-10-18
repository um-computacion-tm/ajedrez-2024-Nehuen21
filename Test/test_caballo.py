import unittest

from game.board import Board
from game.caballo import Caballo

class TestCaballo(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__caballo_blanco__ = Caballo("blanco",3,3 )                #Inicializo el caballo en el medio del tablero para mayor claridad en los movimientos
        self.__cabalo_negro__ = Caballo("negro",7,1)

        self.__board__.setear_tablero(3,3,self.__caballo_blanco__)

    
    def test_movimiento_valido(self):
        
        resultado_izquierda = self.__caballo_blanco__.movimiento_valido(4, 1, self.__board__)
        self.assertTrue(resultado_izquierda)

        
        resultado_derecha = self.__caballo_blanco__.movimiento_valido(4, 5, self.__board__)
        self.assertTrue(resultado_derecha)

    def test_movimiento_invalido_fuera_rango(self):
        """Verifica que el caballo no pueda moverse fuera de su patrón válido."""
        destino = (4, 4)
        resultado = self.__caballo_blanco__.movimiento_valido(*destino, self.__board__)
        self.assertFalse(resultado,)




    def test_icono_caballlo_blanco(self):
       self.assertEqual(str(self.__caballo_blanco__), "♘")

    def test_icono_caballo_negro(self):
         self.assertEqual(str(self.__cabalo_negro__), "♞")


if __name__ == '__main__':
    unittest.main()
