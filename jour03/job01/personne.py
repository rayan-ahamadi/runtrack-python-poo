
class Personne : 
    def __init__(self, nom_,age_,ville_object_):
        self.nom = nom_
        self.age = age_
        self.ville = ville_object_
    def ajouterHabitant(self,ville_object_): 
        ville_object_.nbHabitant += 1 

