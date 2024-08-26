
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def foo(x,y):
    pass

class Toto1(): # ceci est une classe
    # variables de classe = communes à tous les objets
    N = 0 # nb de d'objet
    def __init__(self,a,h = 150, nom = 'toto'): #méthode "constructeur" de l'objet Toto1, appelée à la création de l'objet
        # ici l'agrument a est obligatoire (mandatory)
        # l'argument h est optionnel = sa valeur par défaut vaut 150
        print("création de l'objet")
        self.number = Toto1.N
        Toto1.N += 1 # incrémente le nb total d'objets
        self.name = nom
        # variables d'instance = variable de l'object
        self.height = h # cm
        self.age = a # ans
    def setHeight(self, h): # méthode d'instance
        # méthode "setter" -> permet de mettre à jour un champ (attribut = variable de classe)
        # en permettant un contrôle sur la valeur du paramètre
        if h>250 or h<50 : # permet de filter la valeur
            print("invalid")
            return
        self.height = h # actualise la nouvelle taille de l'objet avec le paramètre h
    def __str__(self):
        return " Ceci est l'objet n°"+str(self.number)+" nommé, "+str(self.name)
    def getHeight(self): # méthode lecture
        return self.height # renvoi la taille
    # Press the green button in the gutter to run the script.
    # méthodes get et set
# CREATION D'OBJETS, instance et variables d'objet
# HERITAGE
# EN PRATIQUE ON CREE RAREMENT DE CLASSE à partir de zéro, on fait un héritage.
# dans pygame on écrit souvent:
class Personnage(pygame.Sprite): # on récupère tous les outils de la classe sprite
    pass
pass
class Toto2(Toto1): # la classe Toto2 hérite de toutes les propriétés de la classe Toto1
    def __init__(self,poids = 50, h = 130, a = 7):# constructeur de la classe Toto2
        super().__init__(a=a,h=h,nom = 'Toto2') # appelle le constructeur de la classe "mère" = super classe
        self.poids = 50 #kg
    def __str__(self): # on modifie la méthode __str__ avec une nouvelle méthode = SUR-CHARGE
        # comment récupérer une méthode de la classe Toto1 ( = appelée la super classe = la classe dont on hérite)
        s1 = super().__str__() # méthode de la classe Toto1
        return s1 + ' Voici son age '+str(self.age)+ ' son poids = '+str(self.poids) + ' sa taille = '+str(self.height)

if __name__ == '__main__':
    o1 = Toto1( a = 17, h = 170) # o1 est un objet de type "Toto1" -> on "instancie" la classe
    o2 = Toto1(11,nom=' Tartampion') #crée l'objet o2 avec 11 ans
    print(o1)
    print(o2)
    o3 = Toto2(a = 25)
    print(o3)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
