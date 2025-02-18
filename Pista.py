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
