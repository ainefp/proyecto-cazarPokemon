from Pokemon import Pokemon
from contador_letras import contar_letras

class Biblioteca:
    pokemon: Pokemon
    lista: list

    def __init__(self, pokemon: Pokemon):
        self.pokemon = pokemon
        self.lista = []
    
    def agregar_pokemon(self) -> list:
        self.lista.append(self.pokemon)
        return self.lista
    
    def __str__(self):
        lista = "".join(self.lista)
        print(lista)

ponyta = Pokemon("ponyta", contar_letras("ponyta"), "fuego", 24.5, 1.12)
print(ponyta)

ponyta = Biblioteca(ponyta)
ponyta.agregar_pokemon()


pikachu = Pokemon("pikachu", contar_letras("pikachu"), "electrico", 16.6, 0.98)
print(pikachu)

pikachu = Biblioteca(pikachu)
pikachu.agregar_pokemon()

print(pikachu)