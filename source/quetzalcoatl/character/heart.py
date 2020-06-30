from quetzalcoatl.resources import Resources
from quetzalcoatl.character.basic_character import BasicCharacter


class Heart(BasicCharacter):
    """[summary]
    """
    def __init__(self, x_pos:float, y_pos:float):
        """La comida de Quetzalcoatl debe aparecer en una posición aleatoria dentro del escenario.

        Args:
            x_pos (float): posición inicial del objeto sobre el escenario en el eje horizontal.
            y_pos (float): posición inicial del objeto sobre el escenario en el eje vertical.
        """
        super().__init__(image = Resources.get_heart_animation())
        self.position = x_pos, y_pos