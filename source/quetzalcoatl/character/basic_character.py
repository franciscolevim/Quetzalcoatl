from cocos.sprite import Sprite


class BasicCharacter(Sprite):
    """Molde para generar a los personajes del juego a través de sprites.
    """
    STOP = 0

    def __init__(self, image):
        """Los personajes se crean como objetos estáticos dentro del escenario.

        Args:
            image (pyglet.image.AbstractImage or pyglet.image.Animation)): Imagen que conforma el sprite.
        """
        super().__init__(image)
        self.direction = BasicCharacter.STOP


    def move(self):
        """Los personaje por lo general deben tener asociado un movimiento por el escenario.
        """
        pass

    
        