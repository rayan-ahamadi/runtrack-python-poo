import ville 
import personne


paris = ville.Ville("Paris",1000000)
marseille = ville.Ville("Marseille",861635)

john = personne.Personne("John",45,paris)
myrtille = personne.Personne("Myrtille",4,paris)
chloé = personne.Personne("Chloé",18,marseille)

print("Nombre d'habitant à Paris {} \nNombre d'habitant à Marseille : {}\n".format(paris.getNbHabitant(),marseille.getNbHabitant()))
john.ajouterHabitant(paris)
myrtille.ajouterHabitant(paris)
chloé.ajouterHabitant(marseille)

print("Mise à jour du nombre d'habitant\nNombre d'habitant à Paris {} \nNombre d'habitant à Marseille : {}\n".format(paris.getNbHabitant(),marseille.getNbHabitant()))