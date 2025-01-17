# Función para contar las letras de los nombres

def contar_letras(nombre):
    """_summary_

    Args:
        nombre (_type_): _description_

    Returns:
        _type_: _description_
    """
    total = 0
    for letra in range(len(nombre)):
        total += 1
    
    return total