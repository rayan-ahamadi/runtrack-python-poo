class Voiture:
    def __init__(self,marque_,modele_,annee_,km_,em_):
        self.__marque=marque_
        self.__modele=modele_
        self.__annee=annee_
        self.__kilometrage=km_
        self.__en_marche=em_
        self.__reservoir = 50

    def getMarque(self): 
        return self.__marque
    def getModele(self): 
        return self.__modele
    def getAnnee(self): 
        return self.__annee
    def getKm(self): 
        return self.__kilometrage
    def getEnMarche(self): 
        return self.__en_marche
    def getReservoir(self): 
        return self.__reservoir
    
    def modifMarque(self,marque_): 
        self.__marque = marque_
    def modifModele(self,modele_): 
        self.__modele = modele_
    def modifAnnee(self,annee_): 
        self.__annee = annee_
    def modifKm(self,km_): 
        self.__kilometrage = km_
    def modifEnMarche(self,em_): 
        self.__en_marche = em_
    def modifReservoir(self,reservoir_): 
        self.__reservoir = reservoir_

    def demarrer(self): 
        if self.__en_marche == False and self.__verifier_plein() > 5:
            self.__en_marche = True
            self.__verifier_plein()
            print("La voiture démarre")
        elif self.__en_marche == True:
            print("La voiture a démarré")
        elif self.__verifier_plein < 5:
            print("erreur : la voiture ne peut pas démarrer car peu d'essence")
    def arreter(self):
        if self.__en_marche == True: 
            self.__en_marche = False
        else : 
            print("La voiture est déja à l'arrêt")
    def __verifier_plein(self):
        return self.__reservoir

mcqueen = Voiture("BMW","jsp",1902,39,False)
mcqueen.demarrer()