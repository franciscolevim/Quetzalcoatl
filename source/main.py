from cocos.director import director
from cocos.scene import Scene
from cocos.layer import Layer
from cocos.sprite import Sprite


if __name__ == "__main__":
    """Ejecución del famoso juego de la vibora representado por Quetzalcoatl.
    """
    director.init(caption = 'Quetzalcoatl')
    layer = Layer()
    scene = Scene(layer)
    director.run(scene)