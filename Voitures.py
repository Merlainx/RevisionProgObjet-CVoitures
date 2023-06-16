
# Exercice: creation dune liste de 4 voitures. Affichage des personnes qui conduit ces voitures.
class Voitures:
    def __init__(self, marque, modele, conducteur):
        self.marque = marque
        self.modele = modele
        self.conducteur = conducteur
    def affichage(self):
            print(f"{self.conducteur} est entrain de conduire la voiture {self.marque} {self.modele}.\n")

v1 = Voitures("Lamborghini", "Urus", "Barabara")
v2 = Voitures("Ford", "Mustang", "Wali")
v3 = Voitures("Audi", "SQ9", "Maro")
v4 = Voitures("BMW", "IX", "Danica")
liste_Voitures = [v1, v2, v3, v4]

Voitures.affichage(liste_Voitures[0])
Voitures.affichage(liste_Voitures[1])
Voitures.affichage(liste_Voitures[2])
Voitures.affichage(liste_Voitures[3])