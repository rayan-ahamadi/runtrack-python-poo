class Student:
    def __init__(self, nom_,prenom_,numEtudiant_):
        self.__nom = nom_
        self.__prenom = prenom_
        self.__numEtudiant = numEtudiant_
        self.__nbCredit = 0
        self.__level = ""

    def addCredits(self,nbCredit_):
        if nbCredit_ >= 0 : 
            self.__nbCredit += nbCredit_
        
        
    def __studentsEval(self):
        if self.__nbCredit >= 90: 
            self.__level = "Excellent"
        elif self.__nbCredit >= 80:
            self.__level = "Très bien"
        elif self.__nbCredit == 70:
            self.__level = "Bien"
        elif self.__nbCredit >= 60:
            self.__level = "Passable"
        elif self.__nbCredit < 60:
            self.__level = "insuffisant"


    def getCredits(self):
        return self.__nbCredit
    def getNom(self):
        return self.__nom
    def getPrenom(self):
        return self.__prenom
    def getLevel(self):
        self.__studentsEval()
        return self.__level
    def studentInfo(self): 
        self.__studentsEval()
        return "nom = {}\nprénom = {}\nid = {}\nniveau = {}\n".format(self.__nom,self.__prenom,self.__numEtudiant,self.__level)
        
john = Student("Doe","John",145)
john.addCredits(20)
john.addCredits(40)
john.addCredits(48)
print("Le nombre de point de {} {} est de : {} ".format(john.getPrenom(),john.getNom(),john.getCredits()))
print(john.studentInfo())

