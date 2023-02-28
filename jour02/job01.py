class Rectangle: 
    def __init__(self,longueur_,largeur_) -> None:
        self.long = longueur_ 
        self.larg = largeur_

    def getLarg(self):
        return self.larg
    
    def getLong(self):
        return self.long
    
    def modifLong(self,long):
        self.long = long
    
    def modifLarg(self,larg):
        self.larg = larg

firstRec = Rectangle(10,5)
print("Longueur : ", firstRec.getLong())
print("Largeur : ", firstRec.getLarg())
firstRec.modifLong(11)
firstRec.modifLarg(6)
print("Longueur : ", firstRec.getLong())
print("Largeur : ", firstRec.getLarg())