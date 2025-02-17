def contar_letras(nombre: str) -> int:
    """Función utilizada para contar los caracteres de la cadena que se le pase.

    Args:
        nombre (str): Cadena que recibe

    Returns:
        int: Nº de caracteres de la cadena
    """
    total = 0
    for letra in range(len(nombre)):
        total += 1
    
    return total
