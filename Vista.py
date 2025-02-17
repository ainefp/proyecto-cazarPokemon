from Pista import Pista
import random

class Vista:
    SALIR = 4
    menu = []

    def __init__(self) -> None:
        self.menu = ["Adivinar letra", "Adivinar palabra", "Pedir pista", "Me rindo! ¿Cuál es el pokemon?", "Salir"]

    def bienvenida(self):
        bienvenida = f""
        CARACTER = "="
        LARGO = 37
        
        bienvenida += f"\n{CARACTER * LARGO}\n"
        bienvenida += f"{'Bienvenid@ a Cazar Pokemons'.center(LARGO, ' ')}\n"
        bienvenida += f"{CARACTER * LARGO}\n"

        print(bienvenida)
    
    def mostrar_menu_inicial(self) -> None:
        menu_incial = ["Comenzar juego", "Salir"]
        mostrar = f""
        for i in range(len(menu_incial)):
            mostrar += f"{i+1}. {menu_incial[i]}\n"
        print(mostrar)
    
    def pedir_opcion_inicial(self) -> int:
        opcion = int(input("Introduce una opción: ")) - 1
        while opcion not in [0, 1]:
            opcion = int(input("Por favor, introduce una opción válida: ")) - 1
        
        return opcion

    def mostrar_menu_opcion(self) -> None:
        mostrar = f""
        for i in range(len(self.menu)):
            mostrar += f"{i+1}. {self.menu[i]}\n"
        print(mostrar)
    
    def pedir_opcion_menu(self) -> int:
        opcion = int(input("Introduce una opción: ")) - 1
        while opcion < 0 or opcion > 4:
            opcion = int(input("Por favor, introduce una opción válida: ")) - 1
        
        return opcion
    
    def eleccion(self, eleccion) -> None:
        print(f"{f"Gracias por jugar! Hasta la próxima." if eleccion == self.SALIR else f"\nTu elección ha sido: {self.menu[eleccion - 1]}"}")
    
    def aparecer_pokemon(self) -> None:
        aparicion = f""
        CARACTER = "-"
        LARGO = 37
        C1 = "Ha aparecido un pokemon salvaje"
        C2 = "Adivina su nombre"
        
        aparicion += f"\n{CARACTER * LARGO}\n"
        aparicion += f"{C1.center(LARGO, ' ')}\n" + f"{C2.center(LARGO, ' ')}\n"
        aparicion += f"{CARACTER * LARGO}\n"
            
        print(aparicion)
    
    def pedir_letra(self) -> str:
        letra = input("Introduce la letra: ")
        while len(letra) != 1 or not letra.isalpha():
            letra = input("Por favor, introduce una letra: ")
        
        return letra
    
    def pedir_palabra(self):
        palabra = input("Introduce la palabra: ")
        while not palabra.isalpha():
            palabra = input("Por favor, introduce una palabra: ")

        return palabra
    
    def mostrar_pista(self) -> None:
        pista = Pista()
        print(pista.generar_pista(random.randint(0, 3)))
    
    def rendirse(self, pokemon) -> None:
        print(f"El pokemon es: {pokemon}. Más suerte la próxima vez!")
    
    # def salir(self) -> None:
    #     print("Gracias por jugar! Hasta la próxima.")

    def generar_tablero(self, n_letras: int) -> None:
        print("_ " * n_letras + "\n")
    
    def victoria(self, nombre) -> None:
        print(f"FELICIDADES! El pokemon {nombre} ha sido capturado!\nAhora {nombre} será añadido a la pokedex (segundos de espera)")
    
    def derrota(self, nombre) -> None:
        print(f"El nombre del pokemon era: {nombre}\nHas perdido, te deseo más suerte en la próxima captura.")
    
    def agregado_pokedex(self, nombre) -> None:
        print(f"{nombre} ha sido registrado correctamente :)")

    def volver_a_jugar(self) -> bool:
        respuesta = input("¿Quieres seguir jugando? (s/n): ").lower()

        while respuesta != "s" and respuesta != "n":
            respuesta = input("Por favor, introduzca una respuesta válida (s/n): ").lower()

        return respuesta == "s"
