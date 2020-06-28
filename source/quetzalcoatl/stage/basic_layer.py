from cocos.director import director
from cocos.layer import Layer
from cocos.euclid import Vector2

import random
from pyglet.window import key
from collections import defaultdict

from quetzalcoatl.character.snake import Snake
from quetzalcoatl.character.heart import Heart


class BasicLayer(Layer):
    """Capa principal del escenario, que desplegará la interacción visual del juego con el usuario.
    """
    is_event_handler = True
    __exists_heart = False


    def __init__(self):
        super().__init__()        
        self.window_width, self.window_height = director.get_window_size()

        self.top_limit, self.bottom_limit = self.window_height, 0
        self.left_limit, self.right_limit = 0, self.window_width

        self.snake = Snake(x_pos = self.window_width * 0.50, y_pos = self.window_height * 0.50)
        self.add(self.snake)

        self.schedule(self.update)


    def on_key_press(self, symbol, _):
        self.snake.direction = symbol


    def update(self, delta_t):
        """Actualiza el estado de todos los elementos de la capa.
        """
        self.__move_snake(delta_t)


    def __move_snake(self, offset:float):
        """El personaje principal se deplaza, comenzando por su cabeza y posteriormente cada segmento de su cuerpo.

        Args:
            offset (float): distancia que se ha de desplazar Quetzalcoatl.
        """
        # Si Quetzalcoatl desaparece en el lado izquierdo del escenario tiene que reaparecer del lado derecho.
        if self.snake.direction == key.LEFT and self.snake.position[0] + self.snake.width / 2 <= self.left_limit:
            self.snake.x_position(self.right_limit)
        # Si Quetzalcoatl desaparece en el lado derecho del escenario tiene que reaparecer del lado izquierdo.
        elif self.snake.direction == key.RIGHT and self.snake.position[0] - self.snake.width / 2 >= self.right_limit:
            self.snake.x_position(self.left_limit)
        # Si Quetzalcoatl desaparece arriba del escenario tiene que reaparecer debajo del escenario.
        elif self.snake.direction == key.UP and self.snake.position[1] - self.snake.height / 2 >= self.top_limit:
            self.snake.y_position(self.bottom_limit)
        # Si Quetzalcoatl desaparece debajo del escenario tiene que reaparecer arriba del escenario.
        elif self.snake.direction == key.DOWN and self.snake.position[1] + self.snake.height / 2 <= self.bottom_limit:
            self.snake.y_position(self.top_limit)
        else:
            self.snake.move(offset)

        if not BasicLayer.__exists_heart:
            heart_pos_x = random.uniform(self.left_limit, self.right_limit)
            heart_pos_y = random.uniform(self.bottom_limit, self.top_limit)
            self.heart = Heart(heart_pos_x, heart_pos_y)
            self.add(self.heart)
            BasicLayer.__exists_heart = True
        

