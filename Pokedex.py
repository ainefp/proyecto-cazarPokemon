from Pokemon import Pokemon
import json
# Esta clase tiene una lista para guardar los pokemons conforme se van capturando
# Además, añado los pokemons a un json para que se queden guardados una vez salgas del programa,
#   de esta forma, la pokedex se mantiene guardada y puedes volver a acceder a ella en futuras partidas.
class Pokedex:
    pokemons_capturados: list[Pokemon]

    def __init__(self):
        self.pokemons_capturados = []

    def generar_pokedex(self, nombre_usuario: str) -> None:
        # Genero un json vacío para un usuario en concreto
        pokedex = {}
        
        # Devuelvo el json vacío
        with open(f'{nombre_usuario}_pokedex.json', 'w') as archivo:
            pokedex = json.load(archivo)

        return pokedex

    def agregar_pokemon(self, pokemon: Pokemon, nombre_usuario: str) -> None:
        try:
            with open(f'{nombre_usuario}_pokedex.json', 'r') as archivo:
                pokedex = json.load(archivo)
        except FileNotFoundError:
            pokedex = self.generar_pokedex(nombre_usuario)
        
        nombre = pokemon.nombre
        if nombre in pokedex:
            pokedex[nombre]['cantidad'] += 1
        else:
            pokedex[pokemon.nombre] = {
                'tipo': pokemon.tipo,
                'tamanho': pokemon.tamanho,
                'peso': pokemon.peso,
                'n_pokedex': pokemon.n_pokedex,
                'cantidad': 1
            }
        with open(f'{nombre_usuario}_pokedex.json', 'w') as archivo:
            json.dump(pokedex, archivo, indent=4)