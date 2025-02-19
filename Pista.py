import random
import json

class Pista:
    pistas: list

    def __init__(self):
        self.pistas = [f"El pokemon es de tipo",
                       f"El pokemon pesa",
                       f"El pokemon mide",
                       f"Su número de pokedex es"]

    def pista(self, palabra_secreta: str, n_frase: int) -> str:
        with open('Generar_pokemon.json', 'r') as archivo:
            pokemons = json.load(archivo)
        datos = pokemons[f"{palabra_secreta}"]

        resultado = self.pistas[n_frase]
        match resultado:
            case "El pokemon es de tipo":
                resultado += f" {datos['tipo']}"
            case "El pokemon pesa":
                resultado += f" {datos['peso']} kg"
            case "El pokemon mide":
                resultado += f" {datos['tamanho']} m"
            case _:
                resultado += f" {datos['n_pokedex']}"

        return resultado
    
pista = Pista()
print(pista.pista('Bulbasaur', random.randint(0, 3)))
