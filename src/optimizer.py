import math


class Optimizer:

    def __init__(self, game):
        self.game = game

    def update(self, dt, objects):
        new_objects = []
        for obj in objects:
            object = obj['object']
            position = obj['position']
            angle = position['rotation']
            if object.type != 'boundingBox':
                angle += 2.0*math.pi/360.0
            new_objects.append({
                'object': object,
                'position': {
                    'center': position['center'],
                    'rotation': angle
                }
            })
        return new_objects