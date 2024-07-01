""" On implémente dans ce fichier la classe LinearModel qui aura pour filles
les classes OrdinaryLeastSquare pour la regression des moindres carrées et
Ridge pour la regréssion de ridge"""

import math
from scipy import stats
import matplotlib.pyplot as plt
from Package.module1 import Matrix

class LinearModel():
    """La classe LinearModel admet pour méthode différentes fonctions permettant
     de réaliser une régression linéaire"""
    def __init__(self,intercept = bool):
        self.intercept = intercept

    def predict(self,x_test):
        """ Entrée : des données de test x_test
        Sortie : une liste contenant la prédiction associée """
        self.prediction = x_test*self.beta
        return self.prediction

    def get_coeffs(self):
        """ Entrée : aucune
        Sortie : une liste contenant le vecteur beta"""
        beta = self.beta
        if self.intercept is True:
            return f"Coefficients (la constante fait parti du modèle):\n\
        Intercept = {beta.data[0][0]} \n        Incomes = {beta.data[1][0]}\n\
        Miles = {beta.data[2][0]} \n        MPC = {beta.data[3][0]} \n\
        Tax = {beta.data[4][0]} \n        Dlic = {beta.data[5][0]}"
        return f"Coefficients (la constante ne fait pas partie du modèle): \n\
        Incomes = {beta.data[0][0]} \n        Miles = {beta.data[1][0]} \n\
        MPC = {beta.data[2][0]} \n        Tax = {beta.data[3][0]} \n\
        Dlic = {beta.data[4][0]}"


    def determination_coefficient(self, x_data, y_data):
        """ Entrée : les données explicatives(x) et les données à expliquer (y).
        Sortie : Coefficient de détermination (r_carre)"""
        lines = y_data.get_lines()
        prediction = self.prediction
        if self.intercept is False:
            num = 0
            den = 0
            for elem,val in zip(prediction.data, y_data.data):
                num += elem[0]**2
                den += val[0]**2
            return f"Le coefficient de détermination est : {num/den}"
        y_sumcum = 0
        for var in y_data.data:
            y_sumcum += var[0]
        y_mean = y_sumcum/lines  # y_bar
        num = 0
        den = 0
        for elem,val in zip(prediction.data, y_data.data):
            num += (elem[0]-y_mean)**2
            den += (val[0]-y_mean)**2
        return f"Le coefficient de détermination est : {num/den}"

    def interval_conf(self, x_data, y_data, val):
        """ Calcule les intervals de confiances du paramètre beta au niveau 1-val"""
        beta = self.beta
        line, col = x_data.get_size()
        beta_line = beta.get_lines()
        degre = line - col
        quant = stats.t.ppf(1 - val / 2, degre)
        y_chap = x_data*beta  # y chapeau
        x_t = x_data.transpose()
        racine_carre_inv = ((x_t * x_data).inverse()).puissance(1 / 2)
        sigma_est = sum(((y_data - y_chap).puissance(2)).data[0]) / degre  # sigma estimé
        for elem in range(beta_line):
            inf = beta.data[elem][0] - quant * math.sqrt(sigma_est) * racine_carre_inv.data[elem][elem]
            sup = beta.data[elem][0] + quant * math.sqrt(sigma_est) * racine_carre_inv.data[elem][elem]
            print(f"Un intervalle de confiance pour beta{elem} au niveau {1 - val} est: [{inf},{sup}]")

    def visualisation(self,y_data):
        """Réalise le plot entre les valeurs prédites et les valeurs observées"""
        prediction = self.prediction
        plt.plot(y_data.data, prediction.data, 'o')
        plt.plot(prediction.data, prediction.data)
        plt.xlabel("Observed values")
        plt.ylabel("Predicted values")
        plt.show()

class OrdinaryLeastSquares(LinearModel):
    """Cette class permet d'obtenir l'estimateur des moindres carrés ordianires.
    Elle hérite de la classe LinearModel"""
    def __init__(self,intercept = bool):
        super().__init__(intercept)
        self.intercept = intercept

    def fit(self, x_data, y_data):
        """ Entrée : données explicatives(x) et les données à expliquer (y).
        Sortie : aucune
        La fonction se charge de calculer le vecteur beta sans le retourner"""
        if self.intercept is True:
            lines = x_data.get_lines()
            constante = [1 for i in range(lines)]
            if x_data.getcol(0) != constante:
                x_data.addcol(constante, 0)
            x_t = x_data.transpose()
            carre_inv = (x_t * x_data).inverse()
            self.beta = carre_inv * x_t * y_data
        x_t = x_data.transpose()
        carre_inv = (x_t*x_data).inverse()
        self.beta = carre_inv*x_t*y_data

class Ridge(LinearModel):
    """ On implémente une classe Ridge qui permet d'obtenir l'estimateur de ridge.
    Cette classe hérite de la classe LinearModel"""
    def __init__(self, param, intercept = bool):
        super().__init__(intercept)
        self.param = param

    def fit(self, x_data, y_data):
        """ Entrée : données explicatives(x) et les données à expliquer (y).
        Sortie : aucune
        La fonction se charge de calculer le vecteur beta sans le retourner"""
        if self.intercept is True:
            lines, col = x_data.get_size()
            constante = [1 for i in range(lines)]
            if x_data.getcol(0) != constante:
                x_data.addcol(constante,0)
            x_t = x_data.transpose()
            carre = x_t*x_data
            vect = Matrix.mat_id(col)*self.param #le vecteur lamba*Id
            inverse = (carre+vect).inverse()
            self.beta = inverse*x_t*y_data
        lines, col = x_data.get_size()
        x_t = x_data.transpose()
        carre = x_t*x_data
        vect = Matrix.mat_id(col)*self.param #le vecteur lamba*Id
        inverse = (carre+vect).inverse()
        self.beta = inverse*x_t*y_data
