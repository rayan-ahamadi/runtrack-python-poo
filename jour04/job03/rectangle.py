class Rectangle:
    def __init__(self,longueur_,largeur_) :
        self.__longueur = longueur_
        self.__largeur = largeur_
    def périmètre(self):
        return 2*self.__longueur + 2*self.__largeur
    def surface(self):
        return self.__longueur * self.__largeur
    def getDimension(self):
        return "longueur {} \nlargeur {}".format(self.__longueur,self.__largeur)