from cocos.euclid import Vector2
from pyglet.window import key

from quetzalcoatl.resources import Resources
from quetzalcoatl.character.basic_character import BasicCharacter


class Segment(BasicCharacter):
    """Representacion de cada segmento del cuerpo de Quetzalcoalt. 

    El tamaño del cuerpo será determinado de acuerdo a los items que coma el personaje principal.
    """
    def __init__(self, position:Vector2, direction):
        """La posición inical de cada segmento dependerá del tamaño del cuerpo.

        Args:
            position (Vector2): Posición inicial del segmento dentro del escenario.
            speed (Vector2): Velocidad a la que se desplaza el segmento del cuerpo.
            direction: Dirección en la que se dirige el segmento.
        """
        super().__init__(image = Resources.get_segment_image())
        self.position = position
        self.direction = direction


#     def move(self, offset:float):
#         """El movimiento de Quetzalcoatl debe parte de la dirección que el jugador le da, esta dirección partirá de la 
#         cabeza y cada segmento delcuerpo deberá seguir este movimiento.

#         Args:
#             offset (float): diferencia de distancia que se da de un lado a otro.
#         """
#         mov_x = self.position[0] 
#         mov_y = self.position[1]

#         if self.direction == key.LEFT:
#             mov_x += offset * self.speed.x * -1
#         elif self.direction == key.RIGHT:
#             mov_x += offset * self.speed.x * 1

#         elif self.direction == key.UP:
#             mov_y += offset * self.speed.y * 1

#         elif self.direction == key.DOWN:
#             mov_y += offset * self.speed.y * -1

#         self.position = Vector2(mov_x, mov_y)


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
        self.position = x_pos, y_pos

        self.body = []
        for _ in range(3):
            self.grow()


    def grow(self):
        """[summary]
        """
        pos_x = self.position[0] + 0
        pos_y = self.position[1] - (self.height * (len(self.body) + 1))
        position = pos_x, pos_y
        # direction = self.body[-1].direction if len(self.body) > 0 else self.direction
        # segment = Segment(position, self.direction)
        segment = Segment(position, 0)
        self.body.append(segment)


    def move(self):
        """El movimiento de Quetzalcoatl debe parte de la dirección que el jugador le da, esta dirección partirá de la 
        cabeza y cada segmento delcuerpo deberá seguir este movimiento.

        Args:
            offset (float): diferencia de distancia que se da de un lado a otro.
        """
        if self.direction != BasicCharacter.STOP:
            mov_x = self.position[0]
            mov_y = self.position[1]

            indices = range(len(self.body))
            for idx in indices[:0:-1]:
                self.body[idx].position = self.body[idx - 1].position
                self.body[idx].direction = self.body[idx - 1].direction

            self.body[0].position = self.position
            self.body[0].direction = self.direction

            if self.direction == key.LEFT:
                mov_x -= self.width
            elif self.direction == key.RIGHT:
                mov_x += self.width
            elif self.direction == key.UP:
                mov_y += self.height
            elif self.direction == key.DOWN:
                mov_y -= self.height
            self.position = mov_x, mov_y


    def y_position(self, position:float):
        self.position = self.position[0], position


    def x_position(self, position:float):
        self.position = position, self.position[1]


    def change_direction(self, direction):
        """La dirección a la que se desplaza Quetzalcoatl será dada por el jugador desde el teclado, siendo las 
        posibilidades: arriba, abajo, izquierda y derecha.

        En caso de que el cambio de dirección se intente realizar hacía el cuerpo de Quetzalcoatl, la instrucción de 
        cambio será ignorada.

        Args:
            direction: Nueva dirección de desplazamiento.
        """
        if direction == key.UP and (self.position[1] + self.height) != self.body[0].position[1]:
            self.direction = key.UP
        elif direction == key.DOWN and (self.position[1] - self.height) != self.body[0].position[1]:
            self.direction = key.DOWN
        elif direction == key.RIGHT and (self.position[0] + self.width) != self.body[0].position[0]:
            self.direction = key.RIGHT
        elif direction == key.LEFT and (self.position[0] - self.width) != self.body[0].position[0]:
            self.direction = key.LEFT