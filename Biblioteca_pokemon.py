from Pokemon import Pokemon
from contador_letras import contar_letras

# La clase Biblioteca se utiliza para guardar los pokemons del objeto Pokemon
class Biblioteca:
    pokemon: Pokemon
    lista: list = []

    def __init__(self, pokemon: Pokemon):
        self.pokemon = pokemon
        self.lista = Biblioteca.agregar_pokemon(pokemon)
    
    def agregar_pokemon(pokemon: Pokemon) -> list:
        Biblioteca.lista.append(pokemon)
    
    def ver_biblioteca(self):
        lista = "".join(self.lista)
        print(lista)
    
    def __str__(self):
        return Pokemon(self.pokemon)
        

ponyta = Pokemon("ponyta", contar_letras("ponyta"), "fuego", 24.5, 1.12)
ponyta2 = Biblioteca(ponyta)
ponyta2.agregar_pokemon()
#ponyta2.ver_biblioteca()
# print(ponyta)
# print(ponyta2)


pikachu = Pokemon("pikachu", contar_letras("pikachu"), "electrico", 16.6, 0.98)
print(pikachu)

pikachu = Biblioteca(pikachu)
pikachu.agregar_pokemon()
