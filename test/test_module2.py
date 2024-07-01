""" On implémente des tests unitaires pour mymodule2"""

import unittest
from Package.module1 import Matrix
from Package.module2 import LinearModel, OrdinaryLeastSquares, Ridge


class Lineareg(unittest.TestCase):
    """ Classe des unitests"""
    def setUp(self):
        self.lineaire = LinearModel(True)
        self.ols = OrdinaryLeastSquares(True)
        self.ridge = Ridge(0,True)

    def test_intercept(self):
        """ On vérifie qu'intercept est bien un booléen"""
        self.assertTrue(self.lineaire.intercept)
        self.assertTrue(self.ols.intercept)
        self.assertTrue(self.ridge.intercept)

    def test_equal_beta(self):
        """ Test d'égalité des beta pour la regression de ridge et ols """
        x_data= [[6, 2, 3],[3, 7, 6],[0, 9, 9],[3, 4, 1]]
        y_data = [[1],[2],[7],[3]]
        x_data = Matrix(x_data)
        y_data = Matrix(y_data)
        self.ols.fit(x_data, y_data)
        self.ridge.fit(x_data, y_data)
        self.assertAlmostEqual(self.ols.beta.data, self.ridge.beta.data,7)

    def test_instance_class(self):
        """Vérifie que les instances correspondent """
        self.assertIsInstance(self.lineaire, LinearModel)
        self.assertIsInstance(self.ols, OrdinaryLeastSquares)
        self.assertIsInstance(self.ridge, Ridge)

if __name__ == '__main__':
    unittest.main()
