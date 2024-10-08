# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


# from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey): 
    radius = 5
    def __init__(self, x, y):
        Prey.__init__(self, x, y, Floater.radius*2, Floater.radius*2, 0, 5)
        self.randomize_angle()
    
    def update(self, model):
        self.move()
        x = random()
        if x <= 3:
            speed_changed = self.get_speed() + random() - 5
            angle_changed = self.get_angle() + random() - 5
            if 3 < speed_changed < 7:
                self.set_velocity(speed_changed, angle_changed)
        self.wall_bounce()
        
    def display(self,canvas):
        canvas.create_oval(self._x-Floater.radius      , self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill='#FF0000')
