import unittest
from unittest.mock import patch, MagicMock
from game.cliente import ClienteAjedrez  
from game.excepciones import PiezaInexistente, MismoColorError, MovimientoInvalido,  NoPodesComerAlRey

class TestClienteAjedrez(unittest.TestCase):   

    def setUp(self):
        self.__cliente__ = ClienteAjedrez() 
    def ejecutar_movimiento_con_error(self, mock_ajedrez, error, mensaje_esperado):
        """Método auxiliar para ejecutar movimientos que disparan excepciones."""
        self.__cliente__.juego = mock_ajedrez
        mock_ajedrez.movimientos.side_effect = error

        with patch('builtins.input', side_effect=['A2', 'A3']), patch('builtins.print') as mock_print:
            result = self.__cliente__.ejecutar_movimiento()
            self.assertFalse(result)
            mock_print.assert_any_call(f"\nError: {mensaje_esperado}\n")

    @patch('game.chess.Ajedrez')
    def test_ejecutar_movimiento_errores(self, mock_ajedrez):
        """Test parametrizado para varios errores de movimiento."""
        errores = [
            (PiezaInexistente("No hay ninguna pieza en la posición."), "No hay ninguna pieza en la posición."),
            (MismoColorError("No puedes mover una pieza de color."), "No puedes mover una pieza de color."),
            (MovimientoInvalido("El movimiento no se pudo completar."), "El movimiento no se pudo completar."),
            (NoPodesComerAlRey("No puedes capturar al rey."), "No puedes capturar al rey."),
        ]

        for error, mensaje in errores:
            with self.subTest(error=error):
                self.ejecutar_movimiento_con_error(mock_ajedrez, error, mensaje)


   
    @patch('builtins.input', side_effect=['3', '2'])
    @patch('builtins.print')
    def test_menu_opcion_invalida(self, mock_print, mock_input):
        """Verifica que se maneje una opción inválida en el menú."""
        self.__cliente__.menu()
        mock_print.assert_any_call("\nOpción inválida. Intente nuevamente.\n")

   
    @patch('builtins.input', side_effect=['2'])
    @patch('builtins.print')
    def test_menu_salir(self, mock_print, mock_input):
        """Verifica que la opción 'Salir' funcione correctamente."""
        self.__cliente__.menu()
        mock_print.assert_any_call("\nJuego terminado.\n")
 

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2'])  
    def test_menu_opcion_salir(self, mock_input, mock_print):
        """Verifica que se salga del menú al seleccionar la opción '2'."""
        self.__cliente__.menu()
        mock_print.assert_any_call("\nJuego terminado.\n")  
   
if __name__ == '__main__':
    unittest.main()
