# A Hunter class is derived from a Pulsator and then Mobile_Simulton base.
#   It inherits updating+displaying from Pusator/Mobile_Simulton: it pursues
#   any close prey, or moves in a straight line (see Mobile_Simultion).


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):  
    dist_const = 200
    
    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, Pulsator.radius*2, Pulsator.radius*2, 0, 5)
        self.randomize_angle()
        
    def update(self, model):
        condition = (lambda x : isinstance(x, Prey) and self.distance(x.get_location()) <= Hunter.dist_const)
        close_prey = model.find(condition)
        
        prey1 = list(close_prey)[0]
        dist = self.distance(prey1.get_location())

        for prey in close_prey:
            prey_dist = self.distance(prey.get_location())
            if prey_dist <= dist:
                prey1 = prey
                dist = prey_dist
            
        prey1_x, prey1_y = prey1.get_location()
        hunter_x, hunter_y = self.get_location()
        self.set_angle(atan2(prey1_y- hunter_y, prey1_x - hunter_x))
        
        self.move()
        self.wall_bounce()
        
        return Pulsator.update(self, model)