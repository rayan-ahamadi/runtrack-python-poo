class Point:
    def __init__(self,x_,y_):
        self.x = x_
        self.y = y_

    def afficherLesPoints(self): 
        return print("Coordonnées =\n x : {} \n y : {}".format(self.x,self.y))
    
    def afficherX(self) : 
        return print("Coordonnées = x : {}".format(self.x))
    
    def afficherY(self) : 
        return print("Coordonnées = y : {}".format(self.y))
    
    def changerX(self,newX):
        self.x = newX
        return print("Nouvelle valeur de X : {}".format(self.x))
    
    def changerY(self,newY):
        self.y = newY
        return print("Nouvelle valeur de Y : {}".format(self.y))

coord = Point(50,50)

coord.afficherLesPoints()
coord.afficherX()
coord.afficherY()
coord.changerX(42)
coord.changerY(42)

coord.afficherLesPoints()