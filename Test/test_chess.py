import unittest

from game.board import Board
from game.chess import Ajedres
from game.torre import Torre
from game.rey import Rey
from game.excepciones import MismoColorError
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

    def test__print(self):
       self.__ajedres__ = Ajedres()
       self.__ajedres__.__board__.setear_piezas()

       try : 
                self.__ajedres__.mostrar_tablero()
       except Exception as e :
           self.fail(f"imprimir tablero lanzo una excepcion : {e}")

    def test_pieza_correcta_turno_correcto(self):
        """Verifica que se devuelva la pieza si pertenece al jugador del turno actual."""
        
        self.__ajedres__.__turno_actual__ = "BLANCO"
        rey_blanco = Rey("blanco", 0, 4)
        self.__ajedres__.__board__.setear_tablero(0, 4, rey_blanco)

        
        pieza = self.__ajedres__.__board__.obtener_pieza(0, 4)
        print(f"Pieza encontrada: {pieza}, Color: {pieza.decime_color()}")
        print(f"Turno actual: {self.__ajedres__.turno_actual()}")

        
        try:
            pieza_devuelta = self.__ajedres__.validar_pieza_jugador(0, 4)
            self.assertEqual(pieza_devuelta, rey_blanco, "No se devolvió la pieza correcta.")
        except MismoColorError as e:
            self.fail(f"Se lanzó MismoColorError de forma incorrecta: {e}")

    def test_pieza_incorrecta_turno_incorrecto(self):
        """Verifica que se lance MismoColorError si el jugador intenta mover una pieza del color opuesto."""
        
        self.__ajedres__.__turno_actual__ = "NEGRO"
        rey_blanco = Rey("blanco", 0, 4)
        self.__ajedres__.__board__.setear_tablero(0, 4, rey_blanco)

       
        print(f"Turno actual: {self.__ajedres__.turno_actual()}")

        
        with self.assertRaises(MismoColorError) as context:
            self.__ajedres__.validar_pieza_jugador(0, 4)

        
        self.assertIn(
            "No puedes mover una pieza de color blanco. Turno actual: negro",
            str(context.exception),
            "El mensaje de error no es el esperado."
        )
  
if __name__ == "__main__":
    unittest.main()
