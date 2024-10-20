import os
from game.chess import Ajedrez
from game.excepciones import *


class ClienteAjedrez:
    def __init__(self):
        """Inicializa la interfaz con una nueva instancia del juego."""
        self.__juego__ = Ajedrez()
        self.game_over = False

    def menu(self):
        """Despliega el menú principal y maneja la selección del usuario."""
        while True:
            self.mostrar_menu_principal()
            seleccion = input("Seleccione una opción: ")
            print(f"Seleccionado: {seleccion}")  # Debug
            opcion = self.validar_opcion("menu_principal", seleccion)
            print(f"Opción validada: {opcion}")  # Debug
            if opcion == "Opción inválida":
                print("\nOpción inválida. Intente de nuevo.\n")
            elif opcion == "Salir":
                print("\nJuego terminado.\n")
                break
            elif opcion == "Iniciar juego":
                self.iniciar_juego()
                if self.game_over:
                    break

    def mostrar_menu_principal(self):
        """Muestra las opciones del menú principal."""
        print("\n----- Ajedrez UM -----")
        print("1) Iniciar Juego")
        print("2) Salir\n")

    def validar_opcion(self, tipo_menu, opcion):
        """Valida las opciones seleccionadas en diferentes menús."""
        if tipo_menu == "menu_principal":
            if opcion == "1":
                return "Iniciar juego"
            elif opcion == "2":
                return "Salir"
            else:
                return "Opción inválida"


    def iniciar_juego(self):
        """Inicia una nueva partida."""
        self.__juego__ = Ajedrez()
        self.game_over = False
        print("\nComenzando nueva partida...\n")  # Este mensaje debe imprimirse



    
if __name__ == "__main__":
    cliente = ClienteAjedrez()
    cliente.menu()
