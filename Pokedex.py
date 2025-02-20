from Pokemon import Pokemon
class Pokedex:
    pokemons_capturados: list[Pokemon]

    def __init__(self):
        self.pokemons_capturados = []

    def agregar_pokemon(self, pokemon: Pokemon) -> None:
        self.pokemons_capturados.append(pokemon)
