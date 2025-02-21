from Pista import Pista
from time import sleep
import random
import json

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
    
    def mostrar_menu_inicial(self) -> int | str:
        menu_incial = ["Comenzar juego", "Salir"]
        mostrar = f""
        for i in range(len(menu_incial)):
            mostrar += f"{i+1}. {menu_incial[i]}\n"
        print(mostrar)

        opcion = int(input("Introduce una opción: ")) - 1
        while opcion not in [0, 1]:
            opcion = int(input("Por favor, introduce una opción válida: ")) - 1
        if opcion == 1:
            print("\nGracias por jugar! Hasta la próxima.")
            return "salir"
        
        return opcion

    def mostrar_menu_opcion(self) -> None:
        mostrar = f"\n"
        for i in range(len(self.menu)):
            mostrar += f"{i+1}. {self.menu[i]}\n"
        print(mostrar)
    
    def pedir_opcion(self) -> int | str:
        opcion = int(input("\nIntroduce una opción: ")) - 1
        while opcion < 0 or opcion > 4:
            opcion = int(input("Por favor, introduce una opción válida: ")) - 1
        if opcion == Vista.SALIR:
            print("\nGracias por jugar! Hasta la próxima.")
            return "salir"
        
        return opcion + 1
    
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
        letra = input("\nIntroduce la letra: ").lower()
        while len(letra) != 1 or not letra.isalpha():
            letra = input("Por favor, introduce una letra: ").lower()
        
        return letra
    
    def pedir_palabra(self) -> str:
        palabra = input("\nIntroduce la palabra: ").lower()
        while not palabra.isalpha():
            palabra = input("Por favor, introduce una palabra: ").lower()

        return palabra
    
    def mostrar_pista(self, resultado) -> None:
        print(resultado)

    def imprimir_tablero(self, tablero) -> None:
        for i in range(len(tablero)):
            print(tablero[i], end=" ")
        print()
    
    def mensaje_victoria(self, nombre: str) -> None:
        print(f"\nFELICIDADES! El pokemon ha sido capturado!\nAhora {nombre} será añadido a la pokedex")
        sleep(0.3)
        print("\nCargando pokemon a la pokedex...")
        sleep(0.5)
        print("\n...")
        sleep(0.5)
        print("\nYa casi hemos terminado...", end="")
    
    def mensaje_derrota(self, nombre: str) -> None:
        print(f"\nEl nombre del pokemon era: {nombre}\nHas perdido, te deseo más suerte en la próxima captura.")

    def mensaje_rendirse(self, pokemon: str) -> None:
        print(f"\nEl pokemon es: {pokemon}. Más suerte la próxima vez!")
    
    def agregado_pokedex(self, nombre: str) -> None:
        print()
        sleep(1)
        print(f"\n{nombre} ha sido registrado correctamente :)")
    
    def error_agregado(self) -> None:
        print()
        sleep(1)
        print("\nVaya, parece que algo no ha salido bien.")

    def despedida(self) -> None:
        print(f"\n\nHasta la próxima!")

    def volver_a_jugar(self) -> bool:
        respuesta = print(input("\n¿Quieres seguir jugando? (s/n): ").lower())

        while respuesta != "s" and respuesta != "n":
            respuesta = print(input("Por favor, introduzca una respuesta válida (s/n): ").lower())

        return respuesta == "s"
    
    def mostrar_pokemons_capturados(self, nombre_usuario: str) -> str:
        registro = f""
        CARACTER_1 = "="
        CARACTER_2 = "-"
        LARGO_1 = 37
        LARGO_2 = 24
        frase = "Registro de Pokemons capturados"

        try:
            # Cargo los datos del json en una variable
            with open(f'{nombre_usuario}_pokedex.json', 'r') as archivo:  # modo lectura
                pokedex = json.load(archivo)

                #Contamos la cantidad de pokemons que hay
                cantidad = len(pokedex)

                registro += f"\n{CARACTER_1 * LARGO_1}\n"
                registro += f"{frase.center(LARGO_1, ' ')}\n"
                registro += f"{CARACTER_1 * LARGO_1}\n"
                
                for pokemon in pokedex:
                    datos = pokedex[pokemon]
                    if datos['cantidad'] > 1:
                        cantidad += datos['cantidad']-1
                    
                    registro += f"\n{("Nombre: "+str(datos['nombre'])).center(LARGO_1, ' ')}"
                    registro += f"\n{("Tipo: "+str(datos['tipo'])).center(LARGO_1, ' ')}"
                    registro += f"\n{("Cantidad: "+str(datos['cantidad'])).center(LARGO_1, ' ')}\n"
                    registro += f"\n{(CARACTER_2 * LARGO_2).center(LARGO_1, ' ')}\n"
                
                registro += f"\nTotal de Pokemons capturados: {cantidad}\n"

                print(registro)

        except FileNotFoundError:
            print("Aún no has capturado ningún pokemon")
