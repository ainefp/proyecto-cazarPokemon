from Pokemon import Pokemon
from Contador_letras import contar_letras
from Biblioteca import Biblioteca
from Vista import Vista
from Pista import Pista
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
    
    def generar_pista(self) -> str:

    def tablero_vacio(self, n_letras: int) -> list:
        self.tablero_v = ["__"] * n_letras
        return self.tablero_v

    def tablero_relleno(self, palabra: str) -> list:
        for i in range(len(palabra)):
            self.tablero_r.append(palabra[i])
        return self.tablero_r
    
    def actualizar_tablero(self, letra: str, palabra: str) -> list:
        if len(letra) == 1:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    self.tablero_v[i] = letra
        else:
            if palabra == letra:
                self.tablero_v = self.tablero_r
        
        return self.tablero_v
    
    def comprobar_resultado(self) -> bool:
        return self.tablero_v == self.tablero_r

if __name__ == "__main__":
    # EJEMPLO DE EJECUCIÓN:
    juego = Juego()
    juego.vista.bienvenida()
    juego.vista.mostrar_menu_inicial()
    juego.vista.pedir_opcion_inicial()
    juego.cargar_pokemons()
    juego.vista.aparecer_pokemon()
    palabra_secreta = juego.generar_palabra()
    tablero_vacio = juego.tablero_vacio(contar_letras(palabra_secreta))
    juego.vista.imprimir_tablero(tablero_vacio)
    tablero_relleno = juego.tablero_relleno(palabra_secreta)
    pista = Pista()
    
    partida_ganada = False
    # Para comprobar que has ganado se puede hacer:
    while not partida_ganada:
        palabra = juego.vista.pedir_palabra()
        act = juego.actualizar_tablero(palabra, palabra_secreta)
        juego.vista.imprimir_tablero(act)
        partida_ganada = juego.comprobar_resultado()
    
    juego.vista.victoria(palabra_secreta)
