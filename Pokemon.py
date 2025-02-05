class Pokemon:
    nombre: str
    cantidadLetras: int
    tipo: str
    tamanho: float  # en metros
    peso: float  # en kg
    n_pokedex: int

    def __init__(self, nombre, cantidadLetras, tipo, tamanho, peso, n_pokedex):
        self.nombre = nombre
        self.cantidadLetras = cantidadLetras
        self.tipo = tipo
        self.tamanho = tamanho
        self.peso = peso
        self.n_pokedex = n_pokedex

    def __str__(self):
        return f"El pokemon {self.nombre} es de tipo {self.tipo}, mide {self.tamanho}m, pesa {self.peso}kg y su número en la pokedex es {self.n_pokedex}."
