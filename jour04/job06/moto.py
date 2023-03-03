from vehicule import Vehicule

class Moto(Vehicule):
    def __init__(self, marque_, modele_, annee_, prix_):
        Vehicule.__init__(self,marque_, modele_, annee_, prix_)
        self.roue = 2
    def infoVehicule(self):
        return print("Marque : {}\nModèle : {}\nAnnée : {}\nPrix: {}\nNombre de roue : {}".format(self.marque,self.modele,self.annee,self.prix,self.roue))
    def demarrer(self):
        return print("Moto : Attention, je roule")    