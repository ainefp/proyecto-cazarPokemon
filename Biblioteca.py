from Pokemon import Pokemon
from Contador_letras import contar_letras

# La clase Biblioteca se utiliza para guardar los pokemons del objeto Pokemon
class Biblioteca:
    lista: list[Pokemon]

    def __init__(self):
        self.lista = []
    
    def agregar_pokemon(self, pokemon: Pokemon):
        self.lista.append(pokemon)

    def __str__(self):
        resultado = ""
        for pokemon in self.lista:
            resultado += f"{str(pokemon)}\n"
        return resultado
