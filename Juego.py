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

    def __init__(self) -> None:
        self.vista = Vista()
        self.jugador = Jugador((input("Introduce tu nombre: ")))
        self.biblioteca = []
    
    #metodo privado
    def cargar_pokemons(self) -> None:
        with open('Generar_pokemon.json', 'r') as archivo:
            pokemons = json.load(archivo)
        for pokemon in pokemons:
            datos = pokemons[pokemon]
            agregar_pokemon = Pokemon(datos['nombre'], contar_letras(datos['nombre']), datos['tipo'], datos['tamanho'], datos['peso'], datos['n_pokedex'])
            self.biblioteca.append(agregar_pokemon)

    def generar_palabra(self) -> str:
        pokemon_secreto = self.biblioteca[randint(1, len(self.biblioteca))]
        return str(pokemon_secreto.nombre)

if __name__ == "__main__":
    juego = Juego()
    juego.vista.bienvenida()
    juego.vista.mostrar_menu_opcion()
    juego.cargar_pokemons()
    juego.vista.generar_tablero(contar_letras(juego.generar_palabra()))
    