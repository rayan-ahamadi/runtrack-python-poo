from vehicule import Vehicule

class Voiture(Vehicule):
    def __init__(self, marque_, modele_ ,annee_, prix_):
        Vehicule.__init__(self,marque_, modele_ ,annee_, prix_)
        self.portes = 4
    def infoVehicule(self):
         return print("Marque : {}\nModèle : {}\nAnnée : {}\nPrix: {}\nNombre de porte : {}".format(self.marque,self.modele,self.annee,self.prix,self.portes))
    def demarrer(self):
        return print("Voiture : Attention, je roule")    