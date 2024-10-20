import unittest
from unittest.mock import patch
from game.cliente import ClienteAjedrez
class TestCliente(unittest.TestCase):

    def setUp(self):
        self.__cliente__ = ClienteAjedrez()

    @patch("builtins.input", side_effect=["1", "2"])
    def test_menu_seleccion_iniciar_y_salir(self, mock_input):
        """Simula la selección de Iniciar Juego y luego Salir."""
        with patch("builtins.print") as mock_print:
            self.__cliente__.menu()

            # Verifica que las opciones del menú se imprimen correctamente
            mock_print.assert_any_call("\n----- Ajedrez UM -----")
            mock_print.assert_any_call("\nComenzando nueva partida...\n")  # Ajuste aquí
            mock_print.assert_any_call("\nJuego terminado.\n")  # Ajuste aquí



    @patch("builtins.input", side_effect=["3", "2"])
    def test_menu_opcion_invalida(self, mock_input):
        """Simula una opción inválida y luego salir del menú."""
        with patch("builtins.print") as mock_print:
            self.__cliente__.menu()
            # Verifica que se muestra el mensaje de opción inválida
            mock_print.assert_any_call("\nOpción inválida. Intente de nuevo.\n")


    def test_validar_opcion_salir(self):
        """Prueba que la opción '2' devuelva 'Salir'."""
        resultado = self.__cliente__.validar_opcion("menu_principal", "2")
        self.assertEqual(resultado, "Salir")

    @patch("builtins.print")
    def test_iniciar_juego_muestra_mensaje(self, mock_print):
        """Prueba que al iniciar el juego se imprima el mensaje correcto."""
        self.__cliente__.iniciar_juego()
        mock_print.assert_any_call("\nComenzando nueva partida...\n")



        
if __name__ == "__main__":
    unittest.main()

""" self,
     mock_chess_move,
     mock_print,
     mock_input,
 ): #
     chess = Chess()
     play(chess)
     self.assertEqual(mock_input.call_count, 1)
     self.assertEqual(mock_print.call_count, 3)
     self.assertEqual(mock_chess_move.call_count, 0)
 @patch(  # este patch controla lo que hace el input
     'builtins.input',
     side_effect=['1', '1', '2', 'hola'], # estos son los valores que simula lo que ingresaria el usuario
 )
 @patch('builtins.print') # este patch controla lo que hace el print
 @patch.object(Chess, 'move')
 def test_more_not_happy_path(
     self,
     mock_chess_move,
     mock_print,
     mock_input,
 ): #
     chess = Chess()
     play(chess)
     self.assertEqual(mock_input.call_count, 4)
     self.assertEqual(mock_print.call_count, 3)
     self.assertEqual(mock_chess_move.call_count, 0)
 # @patch(  # este patch controla lo que hace el input
 #     'builtins.input',
 #     side_effect=['1', '1', '2', '1'], # estos son los valores que simula lo que ingresaria el usuario
 # )
 # @patch('builtins.print') # este patch controla lo que hace el print
 # @patch.object(
 #     Chess,
 #     'move',
 #     side_effect=InvalidMove(),
 # )
 # def test_invalid_move(
 #     self,
 #     mock_chess_move,
 #     mock_print,
 #     mock_input,
 # ): #
 #     chess = Chess()
 #     play(chess)
 #     self.assertEqual(mock_input.call_count, 4)
 #     self.assertEqual(mock_print.call_count, 2)
 #     self.assertEqual(mock_chess_move.call_count, 1)"""