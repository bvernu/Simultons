# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    count_const = 30
    
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        self.count = 0
    
    def update(self, model):
        eaten_sims = Black_Hole.update(self, model)
        
        if eaten_sims:
            self.change_dimension(len(eaten_sims), len(eaten_sims))
            self.count = 0
        elif self.count == Pulsator.count_const - 1:
            self.change_dimension(-1, -1)
            if self.get_dimension() == (0,0):
                eaten_sims.add(self)
            self.count = 0 
        else:
            self.count += 1
        
        return eaten_sims
    
    
