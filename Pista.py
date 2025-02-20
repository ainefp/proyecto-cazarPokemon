import random
import json

class Pista:
    pistas: list

    def __init__(self):
        self.pistas = [f"El pokemon es de tipo",
                       f"El pokemon pesa",
                       f"El pokemon mide",
                       f"Su número de pokedex es"]

    def pista(self, palabra_secreta: str, n_frase: int) -> None:
        with open('Generar_pokemon.json', 'r') as archivo:
            pokemons = json.load(archivo)
        datos = pokemons[palabra_secreta]

        resultado = self.pistas[n_frase]
        match n_frase:
            case 0:
                resultado += f" {datos['tipo']}"
            case 1:
                resultado += f" {datos['peso']} kg"
            case 2:
                resultado += f" {datos['tamanho']} m"
            case 3:
                resultado += f" {datos['n_pokedex']}"

        print(resultado)
