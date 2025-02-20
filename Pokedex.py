from Pokemon import Pokemon
import json
# Esta clase tiene una lista para guardar los pokemons conforme se van capturando
# Además, añado los pokemons a un json para que se queden guardados una vez salgas del programa,
#   de esta forma, la pokedex se mantiene guardada y puedes volver a acceder a ella en futuras partidas.
class Pokedex:
    registro = list

    def __init__(self):
        self.registro = []

    def generar_pokedex(self, nombre_usuario: str) -> None:
        # Genero un diccionario vacío
        pokedex = {}

        # Registro el nombre de usuario para no sobreescribir datos
        self.registro.append(nombre_usuario)

        if nombre_usuario in self.registro:
            return None
        else:
            # Cargo el diccionario vacío en un archivo json
            # Si no existe el archivo, lo crea
            with open(f'{nombre_usuario}_pokedex.json', 'w') as archivo:  # modo escritura
                json.dump(pokedex, archivo, indent=4)

    def agregar_pokemon(self, pokemon: Pokemon, nombre_usuario: str) -> None:
        try:
            # Cargo los datos del json en una variable
            with open(f'{nombre_usuario}_pokedex.json', 'r') as archivo:  # modo lectura
                pokedex = json.load(archivo)
        except FileNotFoundError:
            pokedex = self.generar_pokedex(nombre_usuario)
        
        nombre = pokemon.nombre
        if nombre in pokedex:
            # Esto para no duplicar pokemons, si existe, se suma 1 a la cantidad
            pokedex[nombre]['cantidad'] += 1
        else:
            pokedex[pokemon.nombre] = {
                'tipo': pokemon.tipo,
                'tamanho': pokemon.tamanho,
                'peso': pokemon.peso,
                'n_pokedex': pokemon.n_pokedex,
                'cantidad': 1
            }
        
        # Cargo los datos en el archivo json
        with open(f'{nombre_usuario}_pokedex.json', 'w') as archivo:
            json.dump(pokedex, archivo, indent=4)

# Aún no funciona del todo
