import copy
from factory import ObjectFactory


class ObjectHandler:

    def __init__(self, game):
        self.game = game
        self.factory = ObjectFactory()
        self.objects = []
        self._make_objects()

    def add_object(self, xc, yc, nodes):
        obj = self.factory.make(nodes)
        self.objects.append({
            'object': obj,
            'position': (xc, yc)
        })
    
    def remove_object(self, node_id):
        if node_id < len(self.objects):
            obj = self.objects.pop(node_id)
            del obj
    
    def update(self, dt):
        cur_objects = copy.deepcopy(self.objects)
        optimizer = self.game.optimizer
        self.objects = optimizer.update(
            dt, cur_objects
        )
        for obj in self.objects:
            object = obj['object']
            position = obj['position']
            object.update(position)

    def draw(self):
        for obj in self.objects:
            object = obj['object']
            position = obj['position']
            object.draw(position)

    def _make_objects(self, filename):
        pass