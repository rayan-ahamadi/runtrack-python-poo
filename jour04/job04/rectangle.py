from forme import Forme
 
class Rectangle(Forme):
    def __init__(self,largeur_,longueur_):
        Forme.__init__(self)
        self.largeur = largeur_
        self.longueur = longueur_

    def aire(self):
        return self.longueur * self.largeur
