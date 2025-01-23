def contar_letras(nombre):
    """Función utilizada para contar los caracteres de la cadena que se le pase.
    Se utilizará para contar las letras de los nombres de pokemons, por ello se llama 'contar_letras'.

    Args:
        nombre (str): Cadena que recibe

    Returns:
        int: Nº de caracteres de la cadena
    """
    total = 0
    for letra in range(len(nombre)):
        total += 1
    
    return total