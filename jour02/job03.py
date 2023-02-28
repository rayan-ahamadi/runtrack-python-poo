class Livre:
    def __init__(self,titre_,auteur_,nbPages_):
        self.__titre = titre_
        self.__auteur =auteur_
        self.__nbPages =nbPages_
        self.__disponible = True
        self.__acquis = False
        
    def getTitre(self):
        return self.__titre
    def getAuteur(self):
        return self.__auteur
    def getNbPages(self):
        return self.__nbPages
    
    def modifTitre(self,titre):
        self.__titre = titre
    def modifAuteur(self,auteur):
        self.__auteur = auteur
    def modifNbPages(self,nbPages):
        if type(nbPages) != int or nbPages < 0 :  
            print("ModifNbPages : Erreur, valeur incorrecte")
        else: 
            self.__nbPages = nbPages
    def verification(self):
        return self.__disponible
    def emprunter(self):
        if self.__disponible:
            self.__disponible = False
            self.__acquis = True
            print("livre emprunté")
        else: 
            print("le livre n'est plus disponible")
    def rendre(self): 
        if self.__acquis:
            self.__disponible = True
            self.__acquis = False
            print("livre rendu")
        else: 
            print("Vous n'avez pas ce livre")


livre = Livre("MHA","Horikoshi",100)
livre.emprunter()
print(livre.verification())
livre.rendre()
print(livre.verification())
