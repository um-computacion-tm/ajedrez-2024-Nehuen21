import os
from game.chess import Ajedrez
from game.excepciones import *


class ClienteAjedrez:
    def __init__(self):
        """Inicializa la interfaz con una nueva instancia del juego."""
        self.juego= Ajedrez()
        self.game_over = False
        self.resultado = None

    def menu(self):
        """
        Muestra el menú principal y maneja la selección del usuario.
        """
        while True:
            self.mostrar_menu_principal()
            seleccion = input("Seleccione una opción: ").strip()
            opcion = self.validar_opcion("menu_principal", seleccion)

            if opcion == "Opción inválida":
                print("\nOpción inválida. Intente nuevamente.\n")
            elif opcion == "Salir":
                print("\nJuego terminado.\n")
                break
            elif opcion == "Iniciar juego":
                self.iniciar_nueva_partida()
                if self.game_over:
                    break
    
    def mostrar_menu_principal(self):
        """Muestra las opciones del menú principal."""
        print("\n----- Ajedrez UM -----")
        print("1) Iniciar Juego")
        print("2) Salir\n")   
        
    def validar_opcion(self, tipo_menu, opcion):
        """
        Valida las opciones del menú.
        """
        if tipo_menu == "menu_principal":
            if opcion == "1":
                return "Iniciar juego"
            elif opcion == "2":
                return "Salir"
            else:
                return "Opción inválida"
        elif tipo_menu == "menu_turno":
            if opcion in ["1", "2", "3"]:
                return opcion
            else:
                return "Opción inválida"


    def iniciar_nueva_partida(self):
        """
        Inicia una nueva partida de ajedrez.
        """
        self.juego = Ajedrez()
        self.game_over = False
        self.resultado = None
        self.loop_juego()
    
    def loop_juego(self):
        """
        Ejecuta el bucle principal del juego hasta que termine.
        """
        while not self.game_over:
            self.mostrar_tablero_y_turno()
    
            try:
                origen, destino = self.obtener_movimiento_usuario()
                resultado = self.juego.movimientos(origen, destino)
    
                if resultado in ["Victoria Blanca", "Victoria Negra", "Empate"]:
                    print(f"\n{resultado}\nJuego terminado.\n")
                    self.game_over = True
    
            except (PiezaInexistente, MismoColorError, MovimientoInvalido, PosicionError) as e:
                print(f"\nError: {e}\n")
            except Exception as e:
                print(f"\nError inesperado: {e}\n")



    def mostrar_tablero_y_turno(self):
        """
        Muestra el tablero y el turno actual.
        """
        self.limpiar_terminal()
        print(f"\nTurno de {self.juego.turno_actual()}\n")
        self.juego.mostrar_tablero()


    def obtener_movimiento_usuario(self):
        """
        Solicita al usuario las coordenadas de origen y destino.
        """
        print('\nIngrese su movimiento:')
        origen = input('Desde: ').strip()
        destino = input('Hasta: ').strip()
        return origen, destino


    def limpiar_terminal(self):
        """Limpia la pantalla de la terminal."""
        os.system('cls' if os.name == 'nt' else 'clear')





if __name__ == "__main__":
    cliente = ClienteAjedrez()
    cliente.menu()
