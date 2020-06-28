from cocos.euclid import Vector2
from pyglet.window import key

from quetzalcoatl.resources import Resources
from quetzalcoatl.character.basic_character import BasicCharacter


class Segment(BasicCharacter):
    """Representacion de cada segmento del cuerpo de Quetzalcoalt. 

    El tamaño del cuerpo será determinado de acuerdo a los items que coma el personaje principal.
    """
    def __init__(self, position:Vector2):
        """La posición inical de cada segmento dependerá del tamaño del cuerpo.

        Args:
            position (Vector2): Posición inicial del segmento dentro del escenario..
        """
        super().__init__(image = Resources.get_segment_image(), position = position)
        self.speed = Vector2(350.00, 350.00)


class Snake(BasicCharacter):
    """Quetzalcoatl es el personaje principal del juego, del cual tendremos el control.
    """
    def __init__(self, x_pos:float, y_pos:float):
        """La creación de Quetzalcoatl será solo de la cabeza ubicado en el centro del escenario.

        Args:
            x_pos (float): posición inicial del objeto sobre el escenario en el eje horizontal.
            y_pos (float): posición inicial del objeto sobre el escenario en el eje vertical.
        """
        super().__init__(image = Resources.get_head_image())
        self.position = Vector2(x_pos, y_pos)
        self.speed = Vector2(120.00, 120.00)

        self.body = []


    def move(self, offset:float):
        """El movimiento de Quetzalcoatl debe parte de la dirección que el jugador le da, esta dirección partirá de la 
        cabeza y cada segmento delcuerpo deberá seguir este movimiento.

        Args:
            offset (float): diferencia de distancia que se da de un lado a otro.
        """
        mov_x = self.position[0] 
        mov_y = self.position[1]

        if self.direction == key.LEFT:
            mov_x += offset * self.speed.x * -1
        elif self.direction == key.RIGHT:
            mov_x += offset * self.speed.x * 1

        elif self.direction == key.UP:
            mov_y += offset * self.speed.y * 1

        elif self.direction == key.DOWN:
            mov_y += offset * self.speed.y * -1

        self.position = Vector2(mov_x, mov_y)


    def y_position(self, position:float):
        self.position = self.position[0], position


    def x_position(self, position:float):
        self.position = position, self.position[1]

        
