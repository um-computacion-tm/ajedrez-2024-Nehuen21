import unittest
from game.rey import Rey
from game.board import Board
class TestRey(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__rey_blanco__ = Rey("blanco",0,4)
        self.__rey_negro__ = Rey("negro",7,4)
        self.__board__.setear_tablero(0,4,self.__rey_blanco__)
        self.__board__.setear_tablero(7, 4, self.__rey_negro__)

    def verificar_movimientos(self, movimientos, esperado):
        """Verifica una lista de movimientos y si son válidos o inválidos."""
        for x, y in movimientos:
            with self.subTest(x=x, y=y):
                resultado = self.__rey_blanco__.movimiento_valido(x, y, self.__board__)
                self.assertEqual(resultado, esperado)

    def verificar_movimientos(self, movimientos, esperado):
        """Verifica una lista de movimientos y si son válidos o inválidos."""
        for x, y in movimientos:
            with self.subTest(x=x, y=y):
                resultado = self.__rey_blanco__.movimiento_valido(x, y, self.__board__)
                self.assertEqual(resultado, esperado)

    def test_movimientos_validos(self):
        movimientos_validos = [(1, 4), (1, 3), (0, 5), (0, 3)]  # Ejemplo de movimientos válidos
        self.verificar_movimientos(movimientos_validos, True)

    def test_movimientos_invalidos(self):
        movimientos_invalidos = [(2, 4), (2, 2), (3, 3), (4, 4)]  # Ejemplo de movimientos inválidos
        self.verificar_movimientos(movimientos_invalidos, False)


    def test_icono_rey_blanco(self):
       self.assertEqual(str(self.__rey_blanco__), "♔")

    def test_icono_rey_negro(self):
         self.assertEqual(str(self.__rey_negro__), "♚")

    

if __name__ == '__main__':
    unittest.main()