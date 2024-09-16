#Version of prey that has a 10% chance of randomly moving to a
#new place (spawns randomly to somewhere else in the window)

from prey import Prey
from random import random

class Special(Prey):
    radius = 5
    
    def __init__(self, x, y):
        Prey.__init__(self, x, y, Special.radius*2, Special.radius*2, 0, 5)
        self.randomize_angle()
    
    def update(self, model):
        self.move()
        x = random()
        if x < 0.1:
            self.set_location(random()*500, random()*300)
        self.wall_bounce()
        
    def display(self,canvas):
        canvas.create_oval(self._x-Special.radius      , self._y-Special.radius,
                                self._x+Special.radius, self._y+Special.radius,
                                fill='#800080')
