import eleve
import professeur

eleve1 = eleve.Eleve()
prof1 = professeur.Professeur("Informatique")

eleve1.bonjour()
eleve1.allerEnCours()
prof1.modifierAge(40)
prof1.bonjour()
prof1.enseigner()