class Vehicule: 
    def __init__(self,marque_,modele_,annee_,prix_) :
        self.marque = marque_
        self.modele = modele_
        self.annee = annee_
        self.prix = prix_

    def infoVehicule(self):
        return print("Marque : {}\nModèle : {}\nAnnée : {}\nPrix:{}".format(self.marque,self.modele,self.annee,self.prix))
    def demarrer(self):
        return print("Attention, je roule")    