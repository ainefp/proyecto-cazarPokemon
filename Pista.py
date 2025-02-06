from Biblioteca import Biblioteca
from Pokemon import Pokemon
from Contador_letras import contar_letras
from random import randint
import json

class Pista:
    pista: list

    def generar_pista(self):
        pass

    def pedir_pista(self):
        pass

if __name__ == "__main__":
    biblioteca = Biblioteca()
    pikachu = Pokemon("pikachu", contar_letras("pikachu"), "electro", 1.5, 23, 46)
    biblioteca.agregar_pokemon(pikachu)
    pista = Pista()

    # Abrir el json
    with open('Generar_pokemon.json', 'r') as archivo:
        # Cargar los datos en un diccionario
        pokemons = json.load(archivo)

    for clave in pokemons.items():
        pass

    # Acceder a dichos datos
    for pokemon in pokemons:
        datos = pokemons[pokemon]
        print(f"Nombre: {datos['nombre']}\nTipo: {datos['tipo']}\nPeso: {datos['peso']}\n")
    
    # Acceder a uno en específico
    pokemon_buscado = "pikachu"
    for pokemon in pokemons:
        datos = pokemons[pokemon_buscado]
        if datos['nombre'] == "pikachu":
            print(f"Has encontrado a {datos['nombre']}")
            break
