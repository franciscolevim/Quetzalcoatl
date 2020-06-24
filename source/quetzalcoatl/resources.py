from quetzalcoatl.environment import Environment
from quetzalcoatl.utils import path_validators as pathvalid

from pyglet.resource import Loader


class Resources:
    """Aministra los recursos necesarios para el juego.

    Puede haber más de una ruta que contenga recursos.
    """
    __loader = Loader()


    @staticmethod
    def add_path(path:str):
        if pathvalid.exists(path) and path not in Resources.__loader.path:
            Resources.__loader.path.append(path)
            Resources.__loader.reindex()


    @staticmethod
    def remove_path(path:str):
        Resources.__loader.path.remove(path)
        Resources.__loader.reindex()
