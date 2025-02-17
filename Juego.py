from Vista import Vista

class Juego:
    vista = Vista()

    def __init__(self) -> None:
        self.vista = Vista()

if __name__ == "__main__":
    vista = Vista()
    vista.bienvenida()
    vista.mostrar_menu_opcion()
    vista.pedir_letra()
    vista.pedir_palabra()
    vista.aparecer_pokemon()
    vista.victoria("Pikachu")
    vista.agregado_pokedex("Pikachu")

    print(vista.volver_a_jugar())