from Vista import Vista

class Juego:
    vista = Vista()

    def __init__(self) -> None:
        self.vista = Vista()

if __name__ == "__main__":
    vista = Vista()
    print(vista.bienvenida())
    print(vista.mostrar_menu_opcion())
    # eleccion = int(input("Elige una opción: "))
    # print(vista.eleccion(eleccion))
    print(vista.aparecer_pokemon())