class Pokemon:
    nombre: str
    cantidadLetras: int
    tipo: str
    peso: float  # en kg
    tamanho: float  # en metros
    n_pokedex: int

    def __init__(self, nombre, cantidadLetras, tipo, peso, tamanho, n_pokedex):
        self.nombre = nombre
        self.cantidadLetras = cantidadLetras
        self.tipo = tipo
        self.peso = peso
        self.tamanho = tamanho
        self.n_pokedex = n_pokedex

    def __str__(self):
        return f"El pokemon {self.nombre} es de tipo {self.tipo}, pesa {self.peso}kg, mide {self.tamanho}m y su número en la pokedex es {self.n_pokedex}."