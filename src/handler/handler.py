import copy
import yaml

from .factory import ObjectFactory


class ObjectHandler:


    def __init__(self, game, filename):
        self.game = game
        self.objects = []
        self.factory = self._make_object_factory(
            filename
        )

    def setup(self, resolution):
        W, H = resolution
        types = self.factory.types
        self.add_object('boundingBox', H//2, H//2)
        types.remove('boundingBox')

        num_types = len(types)
        size = H // num_types
        xc = (W+H)//2
        for idx, type in enumerate(types):
            yc = idx*size + size//2
            self.add_object(type, xc, yc)
        
    def update(self, dt):
        cur_objects = self.objects
        optimizer = self.game.optimizer
        self.objects = optimizer.update(
            dt, cur_objects
        )

    def draw(self):
        for obj in self.objects:
            object = obj['object']
            position = obj['position']
            object.draw(
                self.game.screen, position
            )

    def add_object(self, type, xc, yc, angle=0.0):
        obj = self.factory.make(type)
        self.objects.append({
            'object': obj,
            'position': {
                'center': [xc, yc],
                'rotation': angle
            }
        })
    
    def remove_object(self, node_id):
        if node_id < len(self.objects):
            obj = self.objects.pop(node_id)
            del obj

    def _make_object_factory(self, filename):
        objects_info = self._safe_load(filename)
        return ObjectFactory(objects_info)

    def _safe_load(self, filename):
        with open(filename, 'r') as file:
            info = yaml.safe_load(file)
        return info['objects']