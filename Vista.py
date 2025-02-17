from Pista import Pista
from Contador_letras import contar_letras
import random

class Vista:
    SALIR = 4
    MENU = []

    def __init__(self):
        self.MENU = ["Adivinar letra", "Adivinar palabra", "Pedir pista", "Me rindo! ¿Cuál es el pokemon?", "Salir"]

    def bienvenida(self) -> str:
        bienvenida = f"======================================\n  Bienvenid@ al juego Cazar Pokemons\n======================================\n"
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
        aparicion = f""
        c1 = "Ha aparecido un pokemon salvaje"
        c2 = "Adivina su nombre"
        
        caracteres = contar_letras(c1)
        aparicion += "-" * 37 + "\n"
        aparicion += " "*3 + c1 + "\n"
        aparicion += " "*10 + c2 + "\n"
        aparicion += "-" * 37 + "\n"
            
        return aparicion
    
    def pedir_letra(self):
        return input("Introduce la letra: ")
    
    def pedir_palabra(self):
        return input("Introduce la palabra: ")
    
    def mostrar_pista(self) -> None:
        pista = Pista()
        print(pista.generar_pista(random.randint(0, 3)))
    
    def rendirse(self, pokemon) -> str:
        rendicion = f"El pokemon era: {pokemon}"
        return rendicion
