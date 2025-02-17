from Biblioteca import Biblioteca
from Pokemon import Pokemon
from Contador_letras import contar_letras
import random
import json

class Pista:
    pistas: list

    def __init__(self):
        with open('Generar_pokemon.json', 'r') as archivo:
            # Cargar los datos en un diccionario
            pokemons = json.load(archivo)
    
        # Elegir una clave aleatoria del diccionario
        clave_aleatoria = random.choice(list(pokemons.keys()))

        # Cargar los datos del Pokémon aleatorio en una variable
        pokemon_aleatorio = pokemons[clave_aleatoria]

        self.pistas = [f"El pokemon es de tipo {pokemon_aleatorio['tipo']}",
                       f"El pokemon pesa {pokemon_aleatorio['peso']} kg",
                       f"El pokemon mide {pokemon_aleatorio['tamanho']} m",
                       f"El número de pokedex del pokemon es {pokemon_aleatorio['n_pokedex']}"]

    def generar_pista(self, n_frase: int) -> str:
        resultado = self.pistas[n_frase]
        return resultado

if __name__ == "__main__":
    biblioteca = Biblioteca()
    pikachu = Pokemon("pikachu", contar_letras("pikachu"), "electro", 1.5, 23, 46)
    biblioteca.agregar_pokemon(pikachu)
    pista = Pista()

    # Abrir el json
    with open('Generar_pokemon.json', 'r') as archivo:
        # Cargar los datos en un diccionario
        pokemons = json.load(archivo)

    # Acceder a dichos datos
    for pokemon in pokemons:
        datos = pokemons[pokemon]
        print(f"Nombre: {datos['nombre']}\nTipo: {datos['tipo']}\nPeso: {datos['peso']}\n")
    
    # Elegir una clave aleatoria
    clave_aleatoria = random.choice(list(pokemons.keys()))

    # Obtener los datos del Pokémon aleatorio
    pokemon_aleatorio = pokemons[clave_aleatoria]
    
    print(f"¡Has encontrado a {pokemon_aleatorio['nombre']}!")

    n_pista = random.randint(0, 3)
    print(pista.generar_pista(n_pista))
