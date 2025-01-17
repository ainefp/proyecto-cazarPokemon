class Pokemon:
    nombre: str
    cantidadLetras: int
    tipo: str
    peso: float  # en kg
    tamanho: float  # en ctm

    def __init__(self, nombre, cantidadLetras, tipo, peso, tamanho):
        self.nombre = nombre
        self.cantidadLetras = cantidadLetras
        self.tipo = tipo
        self.peso = peso
        self.tamanho = tamanho

    def __str__(self):
        return f"El pokemon {self.nombre} es de tipo {self.tipo}, pesa {self.peso}kg y mide {self.tamanho}m."
    