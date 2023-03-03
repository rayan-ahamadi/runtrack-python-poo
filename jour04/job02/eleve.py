import personne

class Eleve(personne.Personne):
    def __init__(self):
        personne.Personne.__init__(self)

    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print("J'ai {} ans".format(self.age))