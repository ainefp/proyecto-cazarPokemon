from Pista import Pista
import random

class Vista:
    SALIR = 4
    MENU = ["Adivinar letra", "Adivinar palabra", "Pedir pista", "Me rindo! ¿Cuál es el pokemon?"]

    def bienvenida(self) -> str:
        bienvenida = f"======================================\n  Bienvenid@ al juego Cazar Pokemons\n======================================"
        return bienvenida
    
    def mostrar_menu_opcion(self) -> str:
        mostrar = f""
        for i in range(len(self.MENU)):
            mostrar += f"{i+1}. {self.MENU[i]}\n"
        return mostrar
    
    def eleccion(self, eleccion) -> str:
        accion = f"\nTu elección ha sido: {self.MENU[eleccion - 1]}"
        return accion
    
    def aparecer_pokemon(self) -> str:
        aparicion = f"\nHa aparecido un pokemon salvaje! Trata de adivinar su nombre"
        return aparicion
    
    def pedir_letra(self):
        return input("Introduce la letra: ")
    
    def mostrar_pista(self) -> None:
        pista = Pista()
        print(pista.generar_pista(random.randint(0, 3)))

if __name__ == "__main__":
    vista = Vista()
    print(vista.bienvenida())
    print(vista.mostrar_menu_opcion())
    eleccion = int(input("Elige una opción: "))
    print(vista.eleccion(eleccion))
    print(vista.aparecer_pokemon())
