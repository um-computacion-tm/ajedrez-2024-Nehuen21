import unittest
from unittest.mock import patch, MagicMock
from game.cliente import ClienteAjedrez  
from game.excepciones import PiezaInexistente, MismoColorError, MovimientoInvalido, PosicionError, NoPodesComerAlRey

class TestClienteAjedrez(unittest.TestCase):    
    @patch('builtins.print')
    @patch('game.chess.Ajedrez')
    def test_ejecutar_movimiento_error_pieza_inexistente(self, mock_ajedrez, mock_print):
        cliente = ClienteAjedrez()
        cliente.juego = mock_ajedrez
        mock_ajedrez.movimientos.side_effect = PiezaInexistente("No hay ninguna pieza en la posición.")
        with patch('builtins.input', side_effect=['A2', 'A3']):
            result = cliente.ejecutar_movimiento()
            self.assertFalse(result)
            mock_print.assert_any_call("\nError: No hay ninguna pieza en la posición.\n")

    @patch('builtins.print')
    @patch('game.chess.Ajedrez')
    def test_ejecutar_movimiento_error_mismo_color(self, mock_ajedrez, mock_print):
        cliente = ClienteAjedrez()
        cliente.juego = mock_ajedrez
        mock_ajedrez.movimientos.side_effect = MismoColorError("No puedes mover una pieza de color.")
        with patch('builtins.input', side_effect=['A2', 'A3']):
            result = cliente.ejecutar_movimiento()
            self.assertFalse(result)
            mock_print.assert_any_call("\nError: No puedes mover una pieza de color.\n")

    @patch('builtins.print')
    @patch('game.chess.Ajedrez')
    def test_ejecutar_movimiento_error_movimiento_invalido(self, mock_ajedrez, mock_print):
        cliente = ClienteAjedrez()
        cliente.juego = mock_ajedrez
        mock_ajedrez.movimientos.side_effect = MovimientoInvalido("El movimiento no se pudo completar.")
        with patch('builtins.input', side_effect=['A2', 'A3']):
            result = cliente.ejecutar_movimiento()
            self.assertFalse(result)
            mock_print.assert_any_call("\nError: El movimiento no se pudo completar.\n")

    @patch('builtins.print')
    @patch('game.chess.Ajedrez')
    def test_ejecutar_movimiento_error_no_podes_comer_al_rey(self, mock_ajedrez, mock_print):
        cliente = ClienteAjedrez()
        cliente.juego = mock_ajedrez
        mock_ajedrez.movimientos.side_effect = NoPodesComerAlRey("No puedes capturar al rey.")
        with patch('builtins.input', side_effect=['A2', 'A3']):
            result = cliente.ejecutar_movimiento()
            self.assertFalse(result)
            mock_print.assert_any_call("\nError: No puedes capturar al rey.\n")

 
    
if __name__ == '__main__':
    unittest.main()
