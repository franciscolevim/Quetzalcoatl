from quetzalcoatl.resources import Resources
from quetzalcoatl.environment import Environment
from quetzalcoatl.stage.basic_layer import BasicLayer
from cocos.director import director
from cocos.scene import Scene
from cocos.layer import Layer



if __name__ == "__main__":
    """Ejecución del famoso juego de la vibora representado por Quetzalcoatl.
    """
    Resources.load_sprites_path()
    director.init(caption = 'Quetzalcoatl', width = 800, height = 600)
    layer = BasicLayer()
    scene = Scene(layer)
    director.run(scene)
