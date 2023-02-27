class Animal: 
    def __init__(self):
        self.age = 0
        self.prenom = ""
    def viellir(self): 
        self.age +=1
        return print("âge de l'animal {}".format(self.age))
    def nommer(self,prenom_):
        self.prenom = prenom_
        return print("L'animal s'appelle désormais {}".format(self.prenom))
animal = Animal()
print(animal.age)
animal.viellir()
animal.nommer("Ace")