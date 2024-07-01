""" Création d'une class Matrix """

class Matrix():
    """Implémentation d'une classe matrice qui regroupe diverses opérations et
    méthodes propres aux matrices"""
    def __init__(self, data):
        if type(data) not in (list, tuple) or not data:
            raise ValueError("Entrez des types valide")
        if type(data[0]) not in (list, tuple):
            raise ValueError("Vérifiez la structure de vos données")

        self.data = data

    def get_size(self):
        """ Retourne la taille d'une matrice"""
        return len(self.data),len(self.data[0])

    def get_lines(self):
        """Retourne le nombre de line de la matrice"""
        return len(self.data)

    def get_col(self):
        """Retourne le nombre de colonne de la matrice"""
        return len(self.data[0])

    def __repr__(self):
        """ Cette fonction permet une représentation visuelle au moment de l'appel
        d'un élément de class Matrix"""
        lines = self.get_lines() #nombre de ligne et de colonne
        repres=""
        for val in range(lines):
            repres=repres+str(self.data[val])
            if val != lines-1:
                repres=repres+"\n"
        return repres

    @staticmethod
    def scalaire(vect_a,vect_b):
        """Calcul le produit vectoriel entre deux vecteurs"""
        scal = 0
        for elem_a,elem_b in zip(vect_a,vect_b): #parcourir les 2 listes en même temps
            scal += elem_a*elem_b
        return scal

    @staticmethod
    def copier(matrice):
        """ Cette fonction effectue une copie indépendante de la matrice en entrée"""
        copie = []
        for elem in matrice:
            lst = elem.copy()
            copie.append(lst)
        return copie

    def transpose(self):
        """ Prends en entrée une matrice et retourne sa transposée"""
        lines, col = self.get_size()
        if lines == col == 1:
            return self.data
        trans = [[0 for elem in range(lines)] for var in range(col)]
        for elem in range(col):
            for var in range(lines):
                trans[elem][var] = self.data[var][elem]
        return Matrix(trans)

    def __add__ (self, autre):
        """ Renvoie la somme de la matrice self et de la matrice autre"""
        if isinstance (autre, Matrix):
            lines, col = self.get_size()
            autre_lines, autre_col = autre.get_size()
            if lines == autre_lines and col == autre_col:
                mat = [[0 for elem in range(lines)] for var in range(col)]
                for elem in range(lines):
                    for var in range(autre_col):
                        mat[elem][var] = self.data[elem][var] + autre.data[elem][var]
                return Matrix(mat)
            raise ValueError("Dimension des matrices incompatibles")
        raise ValueError("L’objet que vous voulez ajouter n’est pas une matrice")

    def __mul__(self,matrice):
        """ Calcul le produit matriciel de self*matrice
        Entrée : Les matrices à multiplier ou une matrice et un entier
        Sortie : Une matrice correspondant au résultat"""
        if not isinstance(matrice,(Matrix,int)):
            raise ValueError("L'élement n'est pas de type matrice")
        if isinstance(matrice,int): #multiplication de la matrice self par un entier
            lines, col = self.get_size() # taille de la matrice self
            res = [[0 for elem in range(col)] for var in range(lines)]
            for elem in range(lines):
                for var in range(col):
                    res[elem][var] = matrice*self.data[elem][var]
            return Matrix(res)
        transposed = matrice.transpose()
        lines, col = self.get_size()
        mat_lines, mat_col = matrice.get_size()
        if not col == mat_lines:
            raise ValueError("Verifiez les tailles des matrices")
        res = [[0 for elem in range(mat_col)] for var in range(lines)]
        for elem in range(lines):
            for var in range(mat_col):
                res[elem][var] = Matrix.scalaire(self.data[elem],transposed.data[var])
        return Matrix(res)

    def __sub__ (self, matrice):
        """ Renvoie la soustraction de la matrice self par la deuxième matrice (self-matrice)"""
        if isinstance (matrice, Matrix):
            lines, col = self.get_size()
            mat_lines, mat_col = matrice.get_size()
            if lines == mat_lines and col == mat_col:
                mat = [[0 for elem in range(lines)] for var in range(mat_lines)]
                for elem in range(lines):
                    for var in range(mat_col):
                        mat[elem][var] = self.data[elem][var] - matrice.data[elem][var]
                return Matrix(mat)
            raise ValueError("Dimension des matrices incompatibles")
        raise ValueError("L’objet que vous voulez ajouter n’est pas une matrice")

    @staticmethod
    def mat_id(nbr):
        """On implémente ici la matrice identité n*n.
        Entrée : la dimension de la matrice
        Sortie : Matrice identité de taille nbr*nbr """
        if nbr <= 0:
            raise ValueError("Entrez une dimension valide")
        if nbr == 1:
            return 1
        mat = [[0 for elem in range(nbr)] for var in range(nbr)]
        for elem in range(nbr):
            for var in range(nbr):
                if elem == var:
                    mat[elem][var] = 1
        return Matrix(mat)

    @staticmethod
    def mineur(matrice,elem,val):
        """ Retourne la sous matrice obtenu en supprimant la i-ème ligne et
        la j-ième colonne de la matrice initiale"""
        lines = len(matrice)
        if lines == 1 :
            return matrice[0][0]
        mat = Matrix.copier(matrice) #copie indépendante de la matrice
        for nbr in range(lines):
            del mat[nbr][val]
        del mat[elem]
        return Matrix(mat)

    def cofacteur(self,elem,val):
        """ Retourne le déterminant de la sous matrice correspondante """
        sous_mat = Matrix.mineur(self.data,elem,val) #extration de la i-ème colonne et de la ligne 0
        return ((-1)**(elem+val))*sous_mat.determinant()

    def determinant(self):
        """ Calcul le déterminant de la matrice """
        lines, col = self.get_size()
        if lines != col:
            raise ValueError("Le déterminant ne peut-être calculé pour une matrice non carrée.")
        if lines == col == 1:
            return self.data[0][0]
        det = 0
        for nbr in range(lines):
            det += self.data[0][nbr]*self.cofacteur(0,nbr)
        return det

    def comatrice(self):
        """ Cette fonction calcule et retourne la comatrice de la matrice en entrée
        Entrée : élément de tyme matrix
        Sortie : la comatrice de la matrice en entrée"""
        lines, col  = self.get_size()
        mat = [[0 for elem in range(col)] for var in range(lines)]
        for elem in range(lines):
            for var in range(col):
                mat[elem][var] = self.cofacteur(elem,var)
        return Matrix(mat)

    def inverse(self):
        """ Calcul et retourne l'inverse de la matrice en entrée"""
        det = self.determinant()
        if det == 0:
            raise ValueError("La matrice n'est pas inversible car elle est de déterminant nul !")
        lines, col  = self.get_size()
        if lines == 1:
            return 1/self.data[0][0]
        mat = self.comatrice() #la comatrice de la matrice en entrée
        comat = mat.transpose() # la transposée de la matrice
        reverse = [[0 for elem in range(col)] for var in range(lines)]
        for elem in range(lines):
            for var in range(col):
                reverse[elem][var] = (comat.data[elem][var])/det
        return Matrix(reverse)

    def puissance(self, num):
        """Retourne la puissance num de tous les éléments de la matrice"""
        lines, col = self.get_size()
        mat = [[0 for elem in range(col)] for var in range(lines)]
        for elem in range(lines):
            for var in range(col):
                mat[elem][var] = (self.data[elem][var]) ** num
        return Matrix(mat)

    def supcol(self,num):
        """ supprime la colonne numéro num de la matrice self"""
        lines, col = self.get_size()
        if num > col-1 :
            raise ValueError("Veuillez entrer un numéro valide de colonne")
        for elem in range(lines):
            del self.data[elem][num]

    def supligne(self,num):
        """ supprime la ligne numéro num de la matrice self"""
        lines = self.get_lines()
        if num > lines-1 :
            raise ValueError("Veuillez entrer un numéro valide de ligne")
        del self.data[num]

    def addcol(self, lst, pos):
        """Ajouter une colonne à la matrice à la position pos """
        lines = self.get_lines()
        if not isinstance(lst,list): #on vérifie le type de l'élément à ajouter
            raise ValueError("La colonne à ajouter doit être une liste")
        if len(lst)!= lines :
            raise ValueError("Vérifiez la taille de la colonne à ajouter")
        nbr = lines
        for elem in lst:
            self.data[lines-nbr].insert(pos, elem)
            nbr -= 1

    def addligne(self, lst, pos):
        """Ajouter une ligne à la matrice à la position pos"""
        col = self.get_col()
        if not isinstance(lst,list): #on vérifie le type de l'élément à ajouter
            raise ValueError("La ligne à ajouter doit être une liste")
        if len(lst)!= col :
            raise ValueError("Vérifiez la taille de la ligne à ajouter")
        mat = self.data
        mat.insert(pos,lst)

    def getcol(self,num):
        """Extraire la colonne numéro num de la matrice self"""
        lines, col = self.get_size()
        if num > col-1:
            raise ValueError("Veuillez entrer un numéro de colonne valide")
        lst = []
        for elem in range(lines):
            lst.append(self.data[elem][num])
        return lst

    def getligne(self,num):
        """Extraire la ligne numéro num de la matrice self"""
        col = self.get_col()
        if num > col-1:
            raise ValueError("Veuillez entrer un numéro de ligne valide")
        return self.data[num]
