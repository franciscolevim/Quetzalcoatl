from quetzalcoatl.utils import path_validators as pathvalid
from os import environ


class Paths:
    """Administra los paths que forman parte del entorno en el que se ejecuta el juego.
    """
    def __init__(self):
        self.__QUETZALCOATL_HOME_ENV = 'QUETZALCOATL'
        self.__QUETZALCOATL_HOME_DIRECTORY = '.'
        self.__RESOURCES_DIRECTORY = 'resources'

        self.home = None


    @property
    def RESOURCES_DIRECTORY(self):
        """Nombre default del directorio donde se pueden encontrar recurso para el juego.
        """
        return self.__RESOURCES_DIRECTORY


    @property
    def home(self):
        """Ubicación principal del programa. Es posible declarar una variable de entorno llamada QUETZALCOATL en la cual se 
        indique esta ubicación.

        El valor por default, en caso de no contar con la variable de entorno QUETZALCOATL o una ruta válida, será el de 
        __QUETZALCOATL_HOME_DIRECTORY.

        Solo puede existir un directorio home.
        """
        return self.__home

    @home.setter
    def home(self, path:str):
        if pathvalid.exists(path):
            self.__home = path
        else:
            try:                
                env_path = environ[self.__QUETZALCOATL_HOME_ENV]
                self.__home = env_path if pathvalid.exists(env_path) else self.__QUETZALCOATL_HOME_DIRECTORY
            except KeyError:
                self.__home = self.__QUETZALCOATL_HOME_DIRECTORY


class Environment:
    """Funcionalidades del entrono de ejecución del juego.
    """
    paths = Paths()