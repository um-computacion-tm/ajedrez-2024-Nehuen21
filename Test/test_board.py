import unittest
from game.torre import Torre
from game.board import Board
from game.caballo import Caballo
from game.alfil import Alfil
from game.rey import Rey
from game.excepciones import AjedrezError, MovimientoInvalido, MovimientoErrorPieza,MismoColorError,PiezaInexistente,NoPodesComerAlRey,PosicionError
class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()  
        self.board.setear_piezas()
        self.__torre_blanco__ = Torre("blanco",0,0)
        self.board.setear_tablero(0,0,self.__torre_blanco__)

    def test_obtener_torre_blanca(self):
        torre = self.board.obtener_pieza(0, 0) 
        self.assertIsInstance(torre, Torre)

    def test_obtener_torre_negra(self):

        torre = self.board.obtener_pieza(7, 7)  
        self.assertIsInstance(torre, Torre)

    def test_obtener_caballo_negro(self):

        caballo = self.board.obtener_pieza(0,1)  
        self.assertIsInstance(caballo, Caballo)

    def test_obtener_caballo_blanco(self):

        caballo = self.board.obtener_pieza(7,1)  
        self.assertIsInstance(caballo, Caballo)

    def test_obtener_alfil_negro(self):

        alfil = self.board.obtener_pieza(0,2)  
        self.assertIsInstance(alfil, Alfil)

    def test_obtener_alfil_blanco(self):

        alfil = self.board.obtener_pieza(7,2)  
        self.assertIsInstance(alfil, Alfil)

    def test_obtener_pieza(self):
        self.assertIsInstance(self.board.obtener_pieza(0,4),Rey)
        self.assertEqual(self.board.obtener_pieza(5,4),None)

    def test_str(self):
        salida_esperada = (
        "      a       b       c       d       e       f       g       h\n"
        "   ┌───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┐\n"
        "  8│   ♖   │   ♘   │   ♗   │   ♕   │   ♔   │   ♗   │   ♘   │   ♖   │  8\n"
        "   ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤\n"
        "  7│   ♙   │   ♙   │   ♙   │   ♙   │   ♙   │   ♙   │   ♙   │   ♙   │  7\n"
        "   ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤\n"
        "  6│       │       │       │       │       │       │       │       │  6\n"
        "   ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤\n"
        "  5│       │       │       │       │       │       │       │       │  5\n"
        "   ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤\n"
        "  4│       │       │       │       │       │       │       │       │  4\n"
        "   ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤\n"
        "  3│       │       │       │       │       │       │       │       │  3\n"
        "   ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤\n"
        "  2│   ♟   │   ♟   │   ♟   │   ♟   │   ♟   │   ♟   │   ♟   │   ♟   │  2\n"
        "   ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤\n"
        "  1│   ♜   │   ♞   │   ♝   │   ♛   │   ♚   │   ♝   │   ♞   │   ♜   │  1\n"
        "   └───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┘\n"
        "      a       b       c       d       e       f       g       h\n"
    )
        self.assertEqual(self.board.__str__(),salida_esperada)
  

    def test_encontrar_pieza_existente(self):
 
        posicion = self.board.encontrar_pieza(self.__torre_blanco__)
        self.assertEqual(posicion, (0, 0, self.__torre_blanco__))
    
    def test_encontrar_pieza_no_existente(self):
  
        pieza_inexistente = Torre("blanco", 1, 1)
        posicion = self.board.encontrar_pieza(pieza_inexistente)
        self.assertIsNone(posicion)

    def test_mover_pieza_valido(self):
        salida = self.board.mover_pieza((1, 1), (3, 1))
        self.assertTrue(salida)

    def test_mover_pieza_invalido(self):
        with self.assertRaises(MovimientoInvalido):
            self.board.mover_pieza((1, 1), (4, 4))


    def test_mover_pieza_valido_con_diferentes_coordenadas(self):
        
        origen = (1, 1)
        destino = (3, 1)
        
        
        resultado = self.board.mover_pieza(origen, destino)
        
       
        self.assertTrue(resultado, "El movimiento de la pieza debería ser válido.")

    def test_mover_a_posicion_ocupada_mismo_color(self):
    
        with self.assertRaises(MismoColorError):
            self.board.mover_pieza((0, 0), (0, 1))


    def test_contar_piezas_inicial(self):
        """Verifica que el conteo inicial de piezas sea correcto."""
        
        contador = self.board.contar_piezas()
        
        self.assertEqual(contador, (16,16))


    def test_no_se_puede_capturar_al_rey(self):
        __rey__ = Rey("negro", 3, 1)
        self.board.setear_tablero(3, 1, __rey__)
        with self.assertRaises(NoPodesComerAlRey):
            self.board.mover_pieza((1, 1), (3, 1))
    
    def test_error_en_borde_del_tablero(self):
        """Verifica que no haya errores al consultar posiciones válidas pero vacías en el borde del tablero."""
        with self.assertRaises(PiezaInexistente):
            self.board.obtener_color((3, 3))

    def test_limpiar_tablero(self):
        """Verifica que el tablero quede vacío después de limpiarlo."""
        self.board.limpiar_tablero()
        for x in range(8):
            for y in range(8):
                self.assertIsNone(self.board.obtener_pieza(x, y))


if __name__ == '__main__':
    unittest.main()
