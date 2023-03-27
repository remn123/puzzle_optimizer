import pygame as pg
import sys

from src.settings import *
from src.handler import *
from src.optimizer import *


class Game:
    

    def __init__(self):
        pg.init()
        self.resolution = (WIDTH, HEIGHT)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.dt = 1
        self.make_game()
    
    def make_game(self):
        self.optimizer = Optimizer(self)
        self.obj_handler = ObjectHandler(self, OBJECTS_FILENAME)
        self.obj_handler.setup((WIDTH, HEIGHT))

    def update(self):
        self.dt = self.clock.tick(FPS)
        self.obj_handler.update(self.dt)
        pg.display.flip()
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.obj_handler.draw()
    
    def on_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            
            # if event.type == pgui.UI_BUTTON_PRESSED:
            #   if event.ui_element == self.ui.widgets.get('button'):
            #       print('Starting Game...')
            #       self.state = 'LOAD_MAP'
    
    def run(self):
        while True:
            self.on_events()
            self.update()
            self.draw()
