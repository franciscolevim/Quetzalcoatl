from cocos.sprite import Sprite
from cocos.euclid import Vector2


class BasicCharacter(Sprite):
    """Molde para generar a los personajes del juego a través de sprites.
    """
    __STOP = 0

    def __init__(self, image):
        """Los personajes se crean como objetos estáticos dentro del escenario.

        Args:
            image (pyglet.image.AbstractImage or pyglet.image.Animation)): Imagen que conforma el sprite.
        """
        super().__init__(image)
        self.speed = Vector2(0.00, 0.00)
        self.direction = BasicCharacter.__STOP


    def move(self, offset:float):
        """Los personaje por lo general deben tener asociado un movimiento por el escenario.

        Args:
            offset (float): distancia que se moverá el personaje.
        """
        pass

    
        