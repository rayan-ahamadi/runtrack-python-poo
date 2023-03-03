from forme import Forme
 
class Cercle(Forme):
    def __init__(self,radius_):
        Forme.__init__(self)
        self.radius = radius_
        

    def aire(self):
        return self.radius * 3.14
