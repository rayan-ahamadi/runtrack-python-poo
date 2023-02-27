class Cercle: 
    def __init__(self,rayon_):
        self.rayon = rayon_
        self.d = self.diametre() 
        self.a = self.aire()
        self.c = self.circonference()
    def diametre(self): 
        return self.rayon*2
    def aire(self):
        return float(self.rayon**2* 3.14)
    def circonference(self): 
        return float(2 * 3.14 * self.rayon)
    
    def afficherInfos(self): 
        print("Information du cercle : ")
        print("Rayon : {}".format(self.rayon))
        print("Diamètre : {}".format(self.d))
        print("Circonference : {}".format(self.c))
        print("Aire : {}".format(self.a))

rond = Cercle(4)
rond2 = Cercle(7)
rond.afficherInfos()
print("\n")
rond2.afficherInfos()