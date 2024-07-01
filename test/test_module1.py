""" On implémente des tests unitaires pour mymodule1"""

import numpy as np
from numpy.linalg import inv, det
from Package.module1 import Matrix

A = [[6,2,3],
     [3,7,6],
     [0,9,9]]
Am = Matrix(A)  #type Matrix
B = [[1,2,3],
     [2,0,6],
     [7,3,0]]
Bm = Matrix(B)  #type Matrix
mat1 = np.array(A)  #type array
mat2 = np.array(B)  #typa array

lst = [1,2,3]
vect = [0,1,4]

def test_size():
    """ Test unitaire pour la taille"""
    assert Am.get_size() == np.shape(mat1)

def test_scalaire():
    """ Test unitaire pour la fonction scalaire de la classe matrice"""
    assert Matrix.scalaire(lst,vect) == np.dot(lst,vect)

def test_transpose():
    """ Test unitaire pour la fonction transpose de la class Matrix """
    assert (np.array((Am.transpose()).data)== mat1.transpose()).all()

def test_add():
    """ Test unitaire pour la fonction __add__ de la class Matrix.
    Am+Bm étant de type matrice, on récupère les données qu'on transforme en arrray.
    On pourra ainsi effectuer la comparaison avec l'array de la fonction somme de numpy"""
    assert (np.array((Am+Bm).data) == mat1 + mat2).all()

def test_mul():
    """Test la fonction mul de la classe Matrix"""
    assert (np.array((Am*Bm).data) == np.dot(mat1,mat2)).all()

def test_sub():
    """Test la fonction sub de la class Matrix"""
    assert (np.array((Am-Bm).data) == mat1 - mat2).all()

def test_id():
    """ Test la fonction mat_id (matrice identité) de la classe Matrix"""
    assert (np.array((Matrix.mat_id(3)).data) == np.eye(3)).all()

def test_det():
    """Test la fonction determinant de la classe Matrix """
    assert Bm.determinant() == round(det(mat2))

def test_inv():
    """Test la fonction inverse de la classe Matrix"""
    assert np.array_equal(np.array((Bm.inverse()).data), inv(mat2))

