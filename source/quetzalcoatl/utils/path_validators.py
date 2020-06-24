"""Utilidades para validar de distintas maneras una ruta según sea necesario.
"""
import os.path
from quetzalcoatl.utils import string_validators as strvalid

def exists(path:str):
    """Valida si una ruta existe.

    Args:
        path (str): Es la ruta que se desea validar.

    Returns:
        bool: Si la ruta es correcta y existe devuelve True, de lo contrario devuelve False.
    """
    return not strvalid.is_empty(path) and os.path.exists(path)
