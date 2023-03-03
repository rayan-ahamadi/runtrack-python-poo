import personne
class Professeur(personne.Personne):
    def __init__(self,matiereEnseignée_):
        personne.Personne.__init__(self)
        self.__matiereEnseignée = matiereEnseignée_
    def enseigner(self):
        print("Le cours de {} va commencer".format(self.__matiereEnseignée))
    