class Personne: 
    def __init__(self,nom_,prenom_):
        self.nom = nom_
        self.prenom = prenom_

    def SePresenter(self): 
        return print("Je suis {} {}".format(self.prenom,self.nom))
    
bruce = Personne("Wayne","Bruce")
tony = Personne("Stark", "Tony")
parker = Personne("Parker", "Peter")

bruce.SePresenter()
tony.SePresenter()
parker.SePresenter()
