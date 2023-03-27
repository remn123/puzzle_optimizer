import numpy as np
import pygame as pg


class Object:


    def __init__(self, type, info):
        self.type = type
        self.info = info
        self.scale = 1

    def update(self):
        pass

    def draw(self, screen, position):
        xc, yc = position['center']
        angle = position['rotation']
        color = self.info.get('color')
        points = self._get_points(xc, yc)
        points = self._rotate(xc, yc, points, angle)
        
        pg.draw.polygon(
            screen, 
            color,
            points
        )
        pg.draw.polygon(
            screen, 
            f'dark{color}',
            points,
            5
        )

    def _get_points(self, xc, yc):
        if self.type == 'boundingBox':
            w = self.info.get('width')
            h = self.info.get('height')
            points = [
                [xc-w//2, yc-h//2],
                [xc-w//2, yc+h//2],
                [xc+w//2, yc+h//2],
                [xc+w//2, yc-h//2]
            ]
            return points
        nodes = self.info.get('nodes')
        points = [
            [xc-nodes[0][0], yc-nodes[0][1]],
            [xc-nodes[1][0], yc+nodes[1][1]],
            [xc+nodes[2][0], yc+nodes[2][1]],
            [xc+nodes[3][0], yc-nodes[3][1]]
        ]
        return points

    def _rotate(self, xc, yc, points, angle):
        points = [(p[0]-xc, p[1]-yc) for p in points]
        points_arr = np.array(points).T
        c, s = np.cos(angle), np.sin(angle)
        rot_mat = np.array(((c, -s), (s, c)))
        new_points_arr = np.matmul(rot_mat, points_arr).T
        new_points = new_points_arr.tolist()
        new_points = [(p[0]+xc, p[1]+yc) for p in new_points]
        return new_points