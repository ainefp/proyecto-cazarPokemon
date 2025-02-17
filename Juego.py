from Vista import Vista
from Jugador import Jugador

class Juego:
    vista = Vista()
    jugador = Jugador(input("Introduce tu nombre: "))

    def __init__(self) -> None:
        self.vista = Vista()

if __name__ == "__main__":
    juego = Juego()
    juego.vista.bienvenida()
    juego.vista.mostrar_menu_opcion()
    