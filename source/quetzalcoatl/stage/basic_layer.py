import cocos.collision_model as cm
from cocos.director import director
from cocos.layer import Layer

import random
from pyglet.window import key
from collections import defaultdict

from quetzalcoatl.character.snake import Snake, Segment
from quetzalcoatl.character.heart import Heart


class BasicLayer(Layer):
    """Capa principal del escenario, que desplegará la interacción visual del juego con el usuario.
    """
    is_event_handler = True
    __exists_heart = False


    def __init__(self):
        super().__init__()        
        self.window_width, self.window_height = director.get_window_size()
        self.top_limit,   self.bottom_limit = self.window_height, 0
        self.right_limit, self.left_limit   = self.window_width,  0

        self.snake = Snake(x_pos = self.right_limit * 0.50, y_pos = self.top_limit * 0.50)
        self.add(self.snake)
        for segment in self.snake.body:
            self.add(segment)

        self.heart_cm = self.__make_collision_manager(self.snake.width * 1.25)
        self.snake_cm = self.__make_collision_manager(self.snake.width * 1.25)
        self.schedule_interval(self.update, 0.2)


    def __make_collision_manager(self, cell_size):
        """Crea un manejador de colisiones.

        Args:
            cell_size: Tamaño de las celdas en las que se divide el escenario para capturar una colisión.
        """
        return cm.CollisionManagerGrid( xmin = self.left_limit,   xmax = self.right_limit,
                                        ymin = self.bottom_limit, ymax = self.top_limit,
                                        cell_width = cell_size, cell_height = cell_size )


    def on_key_press(self, symbol, _):
        """Acciones que se han de realizar al pulsar una tecla.
        """
        self.snake.change_direction(symbol)


    def update(self, delta_t):
        """Actualiza el estado de todos los elementos de la capa.
        """        
        if not self.__snake_collision():
            self.__move_snake(delta_t)
            self.__put_heart()
        else:
            self.__reset_game()


    def __snake_collision(self):
        """Detecta si la cabeza de Quetzalcoatl ha colisionado con su cuerpo.
        """
        self.snake_cm.clear()
        for segment in self.snake.body:
            self.snake_cm.add(segment)
        for segment in self.snake_cm.iter_colliding(self.snake):
            return True
        return False


    def __reset_game(self):
        """Reinicia el juego.
        """
        self.remove(self.heart)
        BasicLayer.__exists_heart = False
        self.snake_cm.clear()
        for segment in self.snake.body:
            self.remove(segment)
        self.remove(self.snake)
        self.snake = Snake(x_pos = self.right_limit * 0.50, y_pos = self.top_limit * 0.50)
        self.add(self.snake)
        for segment in self.snake.body:
            self.add(segment)


    def __put_heart(self):
        """El corazón se coloca en una posición aleatoria dentro del escenario.

        Solo puede haber un corazón en el escenario.
        """        
        if not BasicLayer.__exists_heart:                        
            heart_pos_x = random.uniform(self.left_limit, self.right_limit)
            heart_pos_y = random.uniform(self.bottom_limit, self.top_limit)
            self.heart = Heart(heart_pos_x, heart_pos_y)
            self.add(self.heart)
            BasicLayer.__exists_heart = True
        elif self.heart_cm.they_collide(self.snake, self.heart):
            self.remove(self.heart)
            self.snake.grow()
            self.add(self.snake.body[0])
            BasicLayer.__exists_heart = False


    def __move_snake(self, offset:float):
        """El personaje principal se deplaza, comenzando por su cabeza y posteriormente cada segmento de su cuerpo.

        Args:
            offset (float): distancia que se ha de desplazar Quetzalcoatl.
        """
        # Si Quetzalcoatl desaparece en el lado izquierdo del escenario tiene que reaparecer del lado derecho.
        if self.snake.direction == key.LEFT and self.snake.position[0] <= self.left_limit:
            self.snake.x_position(self.right_limit)            
        # Si Quetzalcoatl desaparece en el lado derecho del escenario tiene que reaparecer del lado izquierdo.
        elif self.snake.direction == key.RIGHT and self.snake.position[0] >= self.right_limit:
            self.snake.x_position(self.left_limit)
        # Si Quetzalcoatl desaparece arriba del escenario tiene que reaparecer debajo del escenario.
        elif self.snake.direction == key.UP and self.snake.position[1] >= self.top_limit:
            self.snake.y_position(self.bottom_limit)
        # Si Quetzalcoatl desaparece debajo del escenario tiene que reaparecer arriba del escenario.
        elif self.snake.direction == key.DOWN and self.snake.position[1] <= self.bottom_limit:
            self.snake.y_position(self.top_limit)
        else:
            self.snake.move() 
