from quetzalcoatl.environment import Environment
from quetzalcoatl.utils import path_validators as pathvalid

from pyglet.resource import Loader


class Resources:
    """Administra los recursos necesarios para el juego.

    Puede haber más de una ruta que contenga recursos.
    """
    __loader = Loader()

    __RESOURCES_DIRECTORY = 'resources'
    __SPRITES_DIRECTORY = 'sprites'
    __HEAD_SPRITE = 'head.png'
    __SEGMENT_SPRITE = 'segment.png'
    __HEART_SPRITE = 'heart.gif'


    @staticmethod
    def load_sprites_path():
        """Cargar la carpeta de sprites que se encuentra dentro del directorio principal.
        """
        Resources.add_path( f'{Environment.paths.home}/{Resources.__RESOURCES_DIRECTORY}/'\
                            f'{Resources.__SPRITES_DIRECTORY}'  )


    @staticmethod
    def add_path(path:str):
        """Carga un directorio que debe contener recursos para el juego. Estos directorios deben existir y puede 
        encontrarse en cualquier ubicación que tenga los permisos necesarios para ser leidos por el programa.

        Args:
            path (str): Ruta del directorio a cargar.
        """
        if pathvalid.exists(path) and path not in Resources.__loader.path:
            Resources.__loader.path.append(path)
            Resources.__loader.reindex()


    @staticmethod
    def remove_path(path:str):
        """Descarta un directorio de recursos.

        Args:
            path (str): Ruta deldirectorio que se va a descartar.
        """
        Resources.__loader.path.remove(path)
        Resources.__loader.reindex()


    @staticmethod
    def get_head_image():
        """Carga la imagen que representa la cabeza del personaje principal.

        Returns:
            Texture: La cabeza de Quetzalcoatl.
        """
        return Resources.__loader.image(Resources.__HEAD_SPRITE)


    @staticmethod
    def get_segment_image():
        """Segmentos de los que se conforma el cuerpo del personaje principla.

        Returns:
            Texture: Segmento del cuerpo de Quetzalcoatl. 
        """
        return Resources.__loader.image(Resources.__SEGMENT_SPRITE)


    @staticmethod
    def get_heart_animation():
        """Sprite animado que representa la comida de Qutzalcoatl: corazones.
        """
        return Resources.__loader.animation(Resources.__HEART_SPRITE)