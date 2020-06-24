from quetzalcoatl.environment import Environment
from quetzalcoatl.utils import path_validators as pathvalid


class Paths:
    """Administra los paths necesarios para acceder a los recursos del juego.
    """
    def __init__(self):
        self.__RESOURCES_DIRECTORY = 'resources'
        self.__resources = [f'{Environment.paths.home}/{self.__RESOURCES_DIRECTORY}']


    @property
    def list(self):
        """Lista de paths en los que se pueden encontrar recursos para el juego.

        Puede haber más de una ruta que contenga recursos. Si existe la variable de entorno QUETZALCOATL la ruta default 
        será QUETZALCOATL/RESOURCES_DIRECTORY;  de lo contrario la ruta default será 
        QUETZALCOATL_HOME_DIRECTORY/RESOURCES_DIRECTORY.
        """
        return self.__resources


class Resources:
    """Funcionalidades de los recursos del juego.
    """
    paths = Paths()

    @staticmethod
    def add(path:str):
        if pathvalid.exists(path) and path not in Resources.paths.list:
            Resources.paths.list.append(path)