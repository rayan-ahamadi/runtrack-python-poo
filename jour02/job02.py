class Livre:
    def __init__(self,titre_,auteur_,nbPages_):
        self.__titre = titre_
        self.__auteur =auteur_
        self.__nbPages =nbPages_
        
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
    

    
livre = Livre("MHA","Horikoshi",100)
print(livre.getAuteur())
livre.modifAuteur("Kishimoto")
livre.modifTitre("Naruto")
livre.modifNbPages(-8)
print("\n")
print(livre.getTitre())
print(livre.getAuteur())
print(livre.getNbPages())

# print(livre.__titre)