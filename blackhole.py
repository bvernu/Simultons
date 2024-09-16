# A Black_Hole is derived from a Simulton base; it updates by finding+removing
#   any objects (derived from a Prey base) whose center is crosses inside its
#   radius (and returns a set of all eaten simultons); it displays as a black
#   circle with a radius of 10 (e.g., a width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):  
    radius = 10
    
    def __init__(self, x, y):
        Simulton.__init__(self, x, y, Black_Hole.radius*2, Black_Hole.radius*2)
    
    def contains(self, xy):
        d = self.distance(xy)
        if d < (self.get_dimension()[0] / 2):
            return True
        else:
            return False
        
    def update(self, model):
        p = (lambda x : isinstance(x, Prey) and self.contains((x._x, x._y)))
        sims = model.find(p)
        # if sims != None:
        #     for s in sims:
        #         model.remove(s)
        return sims
    
    def display(self,canvas):
        canvas.create_oval(self._x - self._width/2      , self._y - self._height/2,
                                self._x + self._width/2, self._y + self._height/2,
                                fill='#000000')
