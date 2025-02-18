from Pokemon import Pokemon
from Contador_letras import contar_letras
from Biblioteca import Biblioteca
from Vista import Vista
from Jugador import Jugador
from random import randint
import json

class Juego:
    vista = Vista
    jugador = Jugador
    biblioteca = Biblioteca
    tablero_v = list[str]
    tablero_r = list[str]

    def __init__(self) -> None:
        self.vista = Vista()
        self.jugador = Jugador((input("Introduce tu nombre: ")))
        self.biblioteca = []
        self.tablero_v = []
        self.tablero_r = []
    
    #metodo privado
    def cargar_pokemons(self) -> None:
        with open('Generar_pokemon.json', 'r') as archivo:
            pokemons = json.load(archivo)
        for pokemon in pokemons:
            datos = pokemons[pokemon]
            agregar_pokemon = Pokemon(datos['nombre'], contar_letras(datos['nombre']), datos['tipo'], datos['tamanho'], datos['peso'], datos['n_pokedex'])
            self.biblioteca.append(agregar_pokemon)

    def generar_palabra(self) -> str:
        return self.biblioteca[randint(1, len(self.biblioteca))].nombre

    def tablero_vacio(self, n_letras: int) -> None:
        self.tablero_v = ["__"] * n_letras
        return self.tablero_v

    def tablero_relleno(self, palabra: str) -> None:
        for i in range(len(palabra)):
            self.tablero_r.append(palabra[i])
        return self.tablero_r
    
    def actualizar_tablero(self, letra: str, palabra: str) -> None:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                self.tablero_v[i] = letra
        
        for i in range(len(self.tablero_v)):
            print(self.tablero_v[i], end=" ")

if __name__ == "__main__":
    # Ejemplo de ejecución:
    juego = Juego()
    juego.vista.bienvenida()
    juego.vista.mostrar_menu_inicial()
    juego.vista.pedir_opcion_inicial()
    juego.cargar_pokemons()
    juego.vista.aparecer_pokemon()
    palabra_secreta = "pikachu" #juego.generar_palabra()
    tablero_vacio = juego.tablero_vacio(contar_letras(palabra_secreta))
    juego.vista.imprimir_tablero(tablero_vacio)
    tablero_relleno = juego.tablero_relleno(palabra_secreta)
    juego.vista.imprimir_tablero(tablero_relleno)
    
    
    # Para comprobar que has ganado se puede hacer:
    while juego.tablero_vacio(contar_letras(palabra_secreta)) != juego.tablero_relleno(palabra_secreta):
        palabra = juego.vista.pedir_letra()
        juego.actualizar_tablero(palabra, palabra_secreta)
