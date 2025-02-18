class Jugador:
    nombre: str
    pokemons_capturados: int
    victorias: int
    derrotas: int

    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.pokemons_capturados = 0
        self.victorias = 0
        self.derrotas = 0
    
    def capturar_pokemon(self) -> None:
        self.pokemons_capturados += 1
    
    def victoria(self) -> None:
        self.victorias += 1
    
    def derrota(self) -> None:
        self.derrotas += 1
    
    def resetear_puntuacion(self) -> None:
        self.pokemons_capturados = 0
        self.victorias = 0
        self.derrotas = 0

    def __str__(self) -> str:
        return f"{self.nombre} ha capturado un total de {self.pokemons_capturados} pokemons."