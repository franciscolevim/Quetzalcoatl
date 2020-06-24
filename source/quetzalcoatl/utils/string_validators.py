"""Utilidades para validar de distintas maneras un texto según sea necesario.
"""

def is_empty(value:str):
    """Valida si un texto tiene un valor None o una cadena en blanco o vacía.

    Args:
        value (str): texto que se desea validar.

    Returns:
        bool: Si el texto no es None ni una cadena en blanco o vacía devuelve False, de lo contrario devuelve True.
    """
    return not (value and value.strip() != '')
