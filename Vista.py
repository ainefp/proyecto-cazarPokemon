from Pista import Pista

class Vista:
    SALIR = 4

    def bienvenida(self) -> None:
        print("======================================")
        print("  Bienvenid@ al juego Cazar Pokemons")
        print("======================================")
    
    def mostrar_menu_opcion(self) -> None:
        print("\n1. Adivinar letra")
        print("2. Adivinar palabra")
        print("3. Pedir pista")
        print("4. Me rindo! ¿Cuál es el pokemon?\n")
    
    def pedir_letra(self):
        return input("Introduce la letra: ")
    
    def mostrar_pista(self):
        pass

if __name__ == "__main__":
    vista = Vista()
    print(vista.bienvenida())
    print(vista.mostrar_menu_opcion())
    vista.pedir_letra()
