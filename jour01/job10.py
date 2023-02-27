class Produit:
    def __init__(self,nom_,prixHT_,TVA_):
        self.nom = nom_
        self.prixHorsT = prixHT_
        self.taxe = TVA_
        self.prixTTC = self.CalculerPrixTTC()

    def CalculerPrixTTC(self): 
        return self.prixHorsT + self.prixHorsT * self.taxe/100
    def name(self):
        return self.nom
    def prixHT(self):
        return self.prixHorsT
    def taxes(self):
        return self.taxe
    def sommePrixTaxe(self):
        return self.prixTTC
    def afficher(self): 
        return {"nom": self.nom,"prixHorsTaxe":self.prixHorsT,"MontantTaxe":self.taxe,"PrixTTC":self.prixTTC }
    
    def modifNom(self,nom_):
        self.nom = nom_
    def modifPrix(self,prixHT_):
        self.prixHorsT = prixHT_

    
    

produit1 = Produit("iPhone 42",1500,20)
produit2 = Produit("Toupie Beyblade", 40,20)
produit3 = Produit("Lodibidon",3,20)

for element in produit1.afficher():
    print("{} : {}".format(element,produit1.afficher()[element]))
print("\n")
for element in produit2.afficher():
    print("{} : {}".format(element,produit2.afficher()[element]))
print("\n")
for element in produit3.afficher():
    print("{} : {}".format(element,produit3.afficher()[element]))
print("\n")

produit3.modifNom("eau")
produit3.modifPrix(1)
for element in produit3.afficher():
    print("{} : {}".format(element,produit3.afficher()[element]))
