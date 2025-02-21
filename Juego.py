from Pokemon import Pokemon
from Contador_letras import contar_letras
from Biblioteca import Biblioteca
from Pokedex import Pokedex
from Vista import Vista
from Pista import Pista
from Jugador import Jugador
from random import randint
import json

class Juego:
    vista = Vista
    jugador = Jugador
    biblioteca = Biblioteca
    pokedex = Pokedex
    tablero_v = list[str]
    tablero_r = list[str]

    def __init__(self) -> None:
        self.vista = Vista()
        self.jugador = Jugador((input("Introduce tu nombre: "))) # hacer comprobaciones
        self.biblioteca = []
        self.tablero_v = []
        self.tablero_r = []
    
    #metodo privado
    def cargar_pokemons(self) -> None:
        with open('Generar_pokemon.json', 'r') as archivo:
            pokemons = json.load(archivo)
        for pokemon in pokemons:
            datos = pokemons[pokemon]
            agregar_pokemon = Pokemon(datos['nombre'], contar_letras(datos['nombre']), datos['tipo'], datos['tamanho'], datos['peso'], datos['n_pokedex'])
            self.biblioteca.append(agregar_pokemon)

    def generar_palabra(self) -> str:
        return self.biblioteca[randint(1, len(self.biblioteca))].nombre
    
    def tablero_vacio(self, n_letras: int) -> list:
        self.tablero_v = ["__"] * n_letras
        return self.tablero_v

    def tablero_relleno(self, palabra: str) -> list:
        for i in range(len(palabra)):
            self.tablero_r.append(palabra[i])
        return self.tablero_r
    
    def actualizar_tablero(self, letra: str, palabra: str) -> list:
        if len(letra) == 1:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    self.tablero_v[i] = letra
        else:
            if palabra == letra:
                self.tablero_v = self.tablero_r
        
        return self.tablero_v
    
    def generar_pista(self, palabra_secreta, n_frase) -> None:
        pista = Pista()
        pista = pista.pedir_pista(palabra_secreta, randint(0,3))
        self.vista.mostrar_pista(pista)

    def comprobar_ronda(self, victoria: bool) -> None:
        if victoria:
            self.jugador.victoria
            self.jugador.capturar_pokemon
        if not victoria:
            self.jugador.derrota
    
    def agregar_pokedex(self, nombre_pokemon: str) -> None:
        try:
            with open('Generar_pokemon.json', 'r') as archivo:
                pokemons = json.load(archivo)
            for pokemon in pokemons:
                datos = pokemons[pokemon]
                agregar_pokemon = Pokemon(datos['nombre'], contar_letras(datos['nombre']), datos['tipo'], datos['tamanho'], datos['peso'], datos['n_pokedex'])
                if agregar_pokemon.nombre == nombre_pokemon:
                    self.pokedex.agregar_pokemon(agregar_pokemon, nombre_pokemon)
                    self.vista.agregado_pokedex(nombre_pokemon)            
        except:
            self.vista.error_agregado()

    def comienzo(self):
        self.vista.bienvenida()
        eleccion = self.vista.mostrar_menu_inicial()
        if eleccion == "salir":
            self.finalizar_juego()

    def jugar_ronda(self):
        self.vista.mostrar_menu_opcion()
        eleccion = self.vista.pedir_opcion()
        if eleccion == "salir":
            self.finalizar_juego()
        self.cargar_pokemons()
        self.vista.aparecer_pokemon()
        palabra_secreta = juego.generar_palabra()
        
        while eleccion != self.vista.SALIR and not self.ronda_finalizada():
            if eleccion == 1:  # Pedir letra
                tablero_vacio = juego.tablero_vacio(contar_letras(palabra_secreta))
                tablero_relleno = juego.tablero_relleno(palabra_secreta)
                juego.vista.imprimir_tablero(tablero_vacio)
                letra = juego.vista.pedir_letra()
                actualizacion = juego.actualizar_tablero(letra, palabra_secreta)
                juego.vista.imprimir_tablero(actualizacion)
            if eleccion == 2:  # Pedir palabra
                tablero_vacio = juego.tablero_vacio(contar_letras(palabra_secreta))
                tablero_relleno = juego.tablero_relleno(palabra_secreta)
                juego.vista.imprimir_tablero(tablero_vacio)
                palabra = juego.vista.pedir_palabra()
                actualizacion = juego.actualizar_tablero(palabra, palabra_secreta)
                juego.vista.imprimir_tablero(actualizacion)
            if eleccion == 3:  # Pedir pista
                juego.generar_pista(palabra_secreta, randint(0, 3))
            if eleccion  == 4:  # Rendirse
                self.vista.mensaje_derrota()
                self.finalizar_juego()
    
    def ronda_finalizada(self) -> bool:
        return self.tablero_v == self.tablero_r
    
    def finalizar_juego(self) -> None:
        print("Hasta pronto!")

    def jugar(self):
        self.jugar_ronda()

if __name__ == "__main__":
    # EJEMPLO DE EJECUCIÓN:
    juego = Juego()
    juego.jugar
