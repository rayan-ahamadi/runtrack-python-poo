from rectangle import Rectangle

class Parallélépipède(Rectangle):
    def __init__(self, longueur_, largeur_,hauteur_):
        Rectangle.__init__(longueur_, largeur_)
        self.hauteur = hauteur_
    def volume(self):
        return self.__longueur * self.__largeur * self.hauteur