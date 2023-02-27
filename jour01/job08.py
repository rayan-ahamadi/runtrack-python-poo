class Personnage:
    def __init__(self,x_,y_):
        self.x= x_
        self.y= y_
        ### Tableau du joueur
        self.tableau = [["","",""],["","",""],["","",""]]
        self.tableau[self.y][self.x] = "-_-"
    

    def gauche(self): 
        if self.x != 0 : 
            self.x -= 1
            self.tableau = [["","",""],["","",""],["","",""]]
            self.tableau[self.y][self.x] = "-_-"

    def droite(self):
        if self.x != 2:  
            self.x += 1
            self.tableau = [["","",""],["","",""],["","",""]]
            self.tableau[self.y][self.x] = "-_-"


    def haut(self):
        if self.y != 0:
            self.y -= 1
            self.tableau = [["","",""],["","",""],["","",""]]
            self.tableau[self.y][self.x] = "-_-"

    def bas(self):
        if self.y < 2:
            self.y += 1
            self.tableau = [["","",""],["","",""],["","",""]]
            self.tableau[self.y][self.x] = "-_-"

    def position(self): 
        return (self.x,self.y)


    def affichTableau(self):
        for i in range(0,len(self.tableau)):
            print(self.tableau[i], end="\n")



joueur = Personnage(0,0)  
joueur.affichTableau()
print("\n \n") 
joueur.bas()
joueur.affichTableau()
print("\n \n") 
joueur.droite()
joueur.affichTableau()
print("\n \n") 
print("Position du joueur: {}".format(joueur.position()))