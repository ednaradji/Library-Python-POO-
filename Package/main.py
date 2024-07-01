""" Ce fichier contient les données extraites sur lesquels sont réalisées des regressions"""

from Package.module1 import Matrix
import Package.module2 as mod2

PATH = "/Users/ednaradji/Documents/fuel2001.txt"

def lire(path):
    """ Ouvre le fichier.txt contenu dans path et le transforme en tableau (liste de liste)"""
    data = open(path, "r")# ouverture du fichier
    data = data.readlines()# renvoie une liste contenant toute les lignes du fichier
    donnees = []
    for ligne in data:
        ligne = ligne.split()
        donnees.append(ligne)
    for ligne in (donnees[1:]):
        for elem in range(len(ligne)-1):
            ligne[elem] = float(ligne[elem])
    return donnees


# ### 2 - Extraction de données
#On appelera le jeu de données dataset

dataset = lire(PATH)
dataset = Matrix(dataset)
len_row, len_col = dataset.get_size()

#Ajout de la var (Target) au jeu de donnée avec la formule 1000 * FuelC / Pop
#Extraction de la colonne Pop
pop = Matrix(dataset.data).getcol(5)
pop = pop[1:]
#Extraction de la colonne FuelC
fuelC = Matrix(dataset.data).getcol(1)
fuelC = fuelC[1:]
#Création de la variable à expliquer liste Target
target = ["Target"]
for i, k in zip(fuelC, pop):
    target.append(1000*i/k)
dataset.addcol(target, len_col)
#On obtient alors la variable Y à expliquer
vect_y = [target[1:]]
Y_t = Matrix(vect_y)
Y = Y_t.transpose()

#Extraction de la matrice X contenant les colonnes (Incomes, Miles, MPC, Tax)
#On désigne par X la matrice des données explicatives
X = Matrix.copier(dataset.data)
X = Matrix(X)
liste = [0, 1, 5, 7, 8]# on stock les index des colonnes à supprimer
for i in sorted(liste, reverse=True):
    X.supcol(i)
X.supligne(0)

#On ajoute à X la colonne Dlic obtenu par la formule : 1000 * Drivers / Pop
#Extraction de la colonne Drivers
drivers = Matrix(dataset.data).getcol(0)
drivers = drivers[1:]  #on retire le premier élément de type str

#Extraction de la colonne Pop
pop = Matrix(dataset.data).getcol(5)
pop = pop[1:]

#Création de la liste Dlic
dlic = []
for i, j in zip(drivers, pop):
    dlic.append(round(1000*i/j, 3))

#Ajout de la colonne Dlic à la matrice X
X.addcol(dlic, 4)

#Séparation de la matrice X (partie train et test)
X_test = X.data[:len_row-11] #sauf les 10 dernière ligne


mod = mod2.OrdinaryLeastSquares(intercept=True)
mod.fit(X, Y)
mod.predict(X)
print(mod.get_coeffs())
print(mod.determination_coefficient(X, Y))
print(mod.interval_conf(X, Y, 0.05))
mod.visualisation(Y)


lin = mod2.Ridge(2, intercept=True)
lin.fit(X, Y)
lin.predict(X)
print(lin.get_coeffs())
print(lin.determination_coefficient(X, Y))
print(lin.interval_conf(X, Y, 0.05))
lin.visualisation(Y)
