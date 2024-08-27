"""1\creation de class transport et deux class filles qui heritent de la
class transport, appelées avion et voiture
2\les attributs de la class transport sont: prix, poids et capacité
3\les attributs de la class avion sont: envergure, portée, catégorie
4\les attributs de la class voiture sont: diamètre des roues, couleur, type carburant
5\methode qui permet de charger le moyen de transport en ajoutant un passager(nom et poids)
6\methode pour savoir le nombre total de moyens de transport + nombre avions + nombre voiture
7\la class transport sans parametre par défaut voiture(10 000,1,5t,4ps,50cm,rouge,diesel)
"""


class Transport():
    nbTransport = 0  # variable de classe

    def __init__(self, prix, poids, cap):
        self.prix = prix
        self.poids = poids
        self.cap = cap
        Transport.nbTransport += 1

    def __str__(self):
        return "Ceci est un moyen de transport de " + str(self.poids) + " kg"


class Voiture(Transport):
    nbVoiture = 0

    def __init__(self, prix=15000, poids=1500, cap=4, diamRoue=50, couleur='#FF0000', carb='diesel'):
        super().__init__(prix, poids, cap)
        self.diamRoue = diamRoue
        self.couleur = couleur
        self.carb = carb
        Voiture.nbVoiture += 1

    def getNbVoiture():  # méthode de classe
        return Voiture.nbVoiture


class Avion(Transport):
    nbAvion = 0

    def __init__(self, prix=15000, poids=1500, cap=4, envergure=30, portee=10000, cat=9):
        super().__init__(prix, poids, cap)
        self.envergure = envergure
        self.portee = portee
        self.cat = cat
        Avion.nbAvion += 1

    def __str__(self):
        return 'ceci est un avion'


t1 = Transport(1500, 80000, 300)
v1 = Voiture()
v2 = Voiture()
a1 = Avion()
a2 = Avion()
print('toto')
print(t1)
print(a1)
print(a1.nbTransport, a1.nbAvion, Avion.nbAvion)
print(Voiture.getNbVoiture())
