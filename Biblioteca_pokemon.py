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
        
if __name__ == "__main__":
    biblioteca = Biblioteca()

    ponyta = Pokemon("ponyta", contar_letras("ponyta"), "fuego", 24.5, 1.12, 77)
    pikachu = Pokemon("pikachu", contar_letras("pikachu"), "electrico", 16.6, 0.98, 25)

    biblioteca.agregar_pokemon(ponyta)
    biblioteca.agregar_pokemon(pikachu)

    print(biblioteca)
