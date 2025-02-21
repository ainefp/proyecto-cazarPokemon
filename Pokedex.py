from Pokemon import Pokemon
import json
# Esta clase tiene una lista para guardar los pokemons conforme se van capturando
# Además, añado los pokemons a un json para que se queden guardados una vez salgas del programa,
#   de esta forma, la pokedex se mantiene guardada y puedes volver a acceder a ella en futuras partidas.
class Pokedex:
    def agregar_pokemon(self, pokemon: Pokemon, nombre_usuario: str) -> None:
        try:
            # Intento cargar los datos del json en una variable, si existe, lo crea
            with open(f'{nombre_usuario}_pokedex.json', 'r') as archivo:  # modo lectura
                pokedex = json.load(archivo)

        except FileNotFoundError:
            # Crea un diccionario vacío
            pokedex = {}
        
        nombre = pokemon.nombre
        
        if nombre in pokedex:
            # Esto para no duplicar pokemons, si existe, se suma 1 a la cantidad
            pokedex[nombre]['cantidad'] += 1
        else:
            pokedex[pokemon.nombre] = {
                'nombre': pokemon.nombre,
                'tipo': pokemon.tipo,
                'tamanho': pokemon.tamanho,
                'peso': pokemon.peso,
                'n_pokedex': pokemon.n_pokedex,
                'cantidad': 1
            }
        
        # Cargo los datos en el archivo json
        with open(f'{nombre_usuario}_pokedex.json', 'w') as archivo:
            json.dump(pokedex, archivo, indent=4)
