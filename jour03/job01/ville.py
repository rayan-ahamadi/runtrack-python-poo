class Ville: 
    def __init__(self,nom_,nbHabitant_):
        self.__nom = nom_
        self.nbHabitant = nbHabitant_

    def getNom(self):
        return self.__nom
    def getNbHabitant(self):
        return self.nbHabitant