from Pista import Pista
import random

class Vista:
    SALIR = 4
    MENU = []

    def __init__(self) -> None:
        self.MENU = ["Adivinar letra", "Adivinar palabra", "Pedir pista", "Me rindo! ¿Cuál es el pokemon?", "Salir"]

    def bienvenida(self):
        print(f"======================================\n  Bienvenid@ al juego Cazar Pokemons\n======================================\n")
    
    def mostrar_menu_opcion(self) -> str:
        mostrar = f""
        for i in range(len(self.MENU)):
            mostrar += f"{i+1}. {self.MENU[i]}\n"
        return mostrar
    
    def eleccion(self, eleccion) -> str:
        print(f"\nTu elección ha sido: {self.MENU[eleccion - 1]}")
    
    def aparecer_pokemon(self) -> str:
        aparicion = f""
        c1 = "Ha aparecido un pokemon salvaje"
        c2 = "Adivina su nombre"
        
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
    
    def rendirse(self, pokemon):
        print(f"El pokemon era: {pokemon}")
    
    def victoria(self, nombre):
        print(f"FELICIDADES! El pokemon {nombre} ha sido capturado!\nAhora {nombre} será añadido a la pokedex (segundos de espera)")
    
    def derrota(self, nombre):
        print(f"El nombre del pokemon era: {nombre}\nHas perdido, te deseo más suerte en la próxima captura.")
    
    def agregado_pokedex(self, nombre):
        print(f"{nombre} ha sido registrado correctamente :)")

    def volver_a_jugar(self) -> bool:
        return input("¿Quieres seguir jugando? (s/n): ").lower() == "s"
