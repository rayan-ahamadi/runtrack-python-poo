class Personne: 
    def __init__(self):
        self.age = 14
    
    def afficherAge(self):
        print("J'ai {} ans".format(self.age))
    
    def modifierAge(self,newAge):
        self.age = newAge
    
    def bonjour(self):
        print("Hello")