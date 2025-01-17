from Pokemon import Pokemon
from contador_letras import contar_letras

class Biblioteca:
    pokemon: Pokemon
    lista: list

    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.lista = []
    
    def agregar_pokemon(self):
        self.lista.append(self.pokemon)
    
    def __str__(self):
        lista = "".join(self.lista)
        print(lista)

ponyta = Pokemon("ponyta", contar_letras("ponyta"), "fuego", 24.5, 1.12)
Biblioteca(ponyta)



print(ponyta)
print(Biblioteca(ponyta))