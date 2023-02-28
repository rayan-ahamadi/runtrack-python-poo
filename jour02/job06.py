class Commande: 
    def __init__(self,numCommande_,listePlat_,statusCommande_):
        self.__numCommande = numCommande_
        self.__listePlat = dict(listePlat_)
        self.__statusCommande = statusCommande_
        self.calcTVA()

    #getter
    def affichCommand(self):
            liste = self.__listePlat
            print("Numéro de commande : {}".format(self.__numCommande))
            for element in liste:
                print("{} : {} euros".format(element, liste[element]) , end="\n")
            print("Status : {}".format(self.__statusCommande))
            print("Total : {0:.2f}".format(self.__calcTotal()))

    #setter
    def ajoutPlat(self,newPlat,prix):
        self.__listePlat[newPlat] = prix

    def annulerCommande(self):
        self.__statusCommande = "Annulée"
        self.__listePlat.clear()
        print("commande annulé")

    def __calcTotal(self):
        sum = 0.0
        for element in self.__listePlat:
            sum = sum + self.__listePlat[element]
        return sum

    def calcTVA(self):
        for element in self.__listePlat:
            calc = self.__listePlat[element]
            self.__listePlat[element] = int(calc) / 100 * 20
         

#Une liste de la nourriture avec leurs prix, commandé par l'objet maCommande 
nourritureCommandé = {
    "nuggets" : 11.3,
    "Cauet Burger" : 10.50, 
    "Coca Cherry" : 2.0, 
}

maCommande = Commande(9751,nourritureCommandé,"en cours")
maCommande.affichCommand()
print("\n")
maCommande.ajoutPlat("Chicken wings",8.0)
maCommande.affichCommand()
print("\n")
maCommande.annulerCommande()
maCommande.affichCommand()

