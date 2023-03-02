class CompteBancaire:
    def __init__(self,numCompte_,nom_,prenom_,solde_,decouvert_):
        self.__numCompte = numCompte_
        self.__nom = nom_
        self.__prenom = prenom_
        self.__solde = solde_
        self.__decouvert = decouvert_

    def afficher(self):
        print("numéro de compte : {}\n nom : {} \n prenom : {} \n solde : {}".format(self.__numCompte,self.__nom,self.__prenom,self.__solde))

    def afficherSolde(self): 
        print("Solde de {} : {}".format(self.__nom, self.__solde))

    def versement(self,montant):
        self.__solde += montant
        print("Versement effectué : +{}".format(montant))   

    def retrait(self,montant):
        if self.__solde > 0 and self.__solde >= montant : 
            self.__solde -= montant
            print("Retrait de {} euros effectué".format(montant))
            print("Solde : {} euros".format(self.__solde))
        if self.__decouvert: 
            self.__solde -= montant
            print("Retrait de {} euros effectué".format(montant))
            print("Solde : {} euros".format(self.__solde))
        else : 
            print("erreur: montant dépassé")

    def agios(self,montant):
        if self.__solde < 0 and self.__decouvert == True: 
            self.__solde -= montant
            print("Agios appliqué, montant prélevé -{}, solde : {}".format(montant,self.__solde))

    def virement(self,montant,client_Object_,libélée): 
        if self.__solde > 0 and self.__solde >= montant : 
            client_Object_.__solde += montant
            self.__solde -= montant
            print("Virement effectuer à {} \n Montant : {} \n Libéllée : {}".format(client_Object_.__nom,montant,libélée))
        else : 
            print("Erreur Le compte émetteur ne peut pas effectuer ce virement")
    
