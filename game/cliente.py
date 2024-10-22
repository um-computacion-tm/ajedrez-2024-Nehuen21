import os
from game.chess import Ajedrez
from game.excepciones import PiezaInexistente, MismoColorError, MovimientoInvalido, PosicionError

class ClienteAjedrez:
    """Interfaz para gestionar el flujo del juego de ajedrez."""

    def __init__(self):
        """Inicializa la interfaz con una instancia de Ajedrez."""
        self.juego = Ajedrez()
        self.game_over = False

    def menu(self):
        """Muestra el menú principal del juego."""
        while True:
            print('\n----- Ajedrez -----')
            print('1) Iniciar Juego')
            print('2) Salir\n')
            
            seleccion = input("Seleccione una opción: ").strip()
            
            if seleccion == "1":
                self.iniciar_juego()
            elif seleccion == "2":
                print("\nJuego terminado.\n")
                break
            else:
                print("\nOpción inválida. Intente nuevamente.\n")

    def iniciar_juego(self):
        """Inicia una nueva partida y ejecuta el bucle principal."""
        self.juego = Ajedrez()
        self.game_over = False

        while not self.game_over:
            self.mostrar_tablero_y_turno()
            if not self.ejecutar_movimiento():
                print("\nMovimiento inválido. Intente nuevamente.\n")

    def mostrar_tablero_y_turno(self):
        """Limpia la terminal y muestra el tablero."""
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\nTurno de {self.juego.turno_actual()}\n")
        self.juego.mostrar_tablero()

    def ejecutar_movimiento(self):
        """Solicita coordenadas y realiza un movimiento."""
        try:
            origen = input('Desde (ej: A2): ').strip()
            destino = input('Hasta (ej: A3): ').strip()

            # Intentar realizar el movimiento
            estado = self.juego.movimientos(origen, destino)

            # Verificar si el juego ha terminado
            if estado != "En curso":
                print(f"\n{estado}\nJuego terminado.\n")
                self.game_over = True

            return True  # Movimiento válido

        except (PiezaInexistente, MismoColorError, MovimientoInvalido, PosicionError) as e:
            print(f"\nError: {e}\n")
            return False  # Movimiento inválido

if __name__ == "__main__":
    cliente = ClienteAjedrez()
    cliente.menu()
