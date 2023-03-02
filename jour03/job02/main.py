import CompteBancaire

compteParker = CompteBancaire.CompteBancaire(254435346,"Parker","Peter",5,True)
compteStark = CompteBancaire.CompteBancaire(294736344,"Stark","Tony",20000000000,True)

compteParker.afficher()
compteParker.retrait(200)
compteParker.agios(5)
print("\n")
compteStark.virement(200,compteParker,"Aide_financière")
compteParker.afficherSolde()
compteStark.afficherSolde()

