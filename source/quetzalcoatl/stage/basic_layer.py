from cocos.director import director
from cocos.layer import Layer
from cocos.euclid import Vector2

from pyglet.window import key
from collections import defaultdict

from quetzalcoatl.character.snake import Snake


class BasicLayer(Layer):
    """Capa principal del escenario, que desplegará la interacción visual del juego con el usuario.
    """
    is_event_handler = True

    def __init__(self):
        super().__init__()
        self.width_window, self.hight_window = director.get_window_size()

        self.snake = Snake(x_pos = self.width_window * 0.50, y_pos = self.hight_window * 0.50)
        self.add(self.snake)

        self.schedule(self.update)


    def on_key_press(self, symbol, _):
        self.snake.direction = symbol


    def update(self, delta_t):
        """Actualiza el estado de la capa.
        """
        self.snake.move(Vector2(delta_t, delta_t))