<font size=7> $\color{maroon}{Présentation \space générale}$ </font>

### Implémentation d'un modèle linéaire avec application des outils vus en cours (POO).

Le nom du package est **Package**.

Il s'inscrit dans un projet de l'UE Python supervisé par Baptiste Gregorutti. Ce projet vise à appliquer les outils vus pendant le cours de "Modèles Linéaires" dirigé par Charlotte Dion. 

<font size=3> $\color{orange}{Contraintes \space imposées :}$ </font>

- Les librairies **sklearn** et **statsmodels** sont proscrites. 
- les libraires **NumPy** et **Pandas** sont autorisées mais des points de bonus seront données si les outils implémentés ne les utilisent pas ou peu.
- Des tests unitaires devront être écrits exécutés avec **pytest**.
- La qualité du code devra être évaluée avec **pylint** et il faudra avoir une note au moins supérieure à 7/10.

Au sein de ce package, seule la librairie **matplotlib** a été utilisée. Des tests unitaires basiques ont été écrits pour chaque fonction. Chaque fichier .py a eu une note supérieur à 7/10 avec **pylint** avec la commande :
        
        pylint *.py */*.py */*/*.py --max-line-length=150

Les contraintes ont donc été respectées.

<font size=7> $\color{maroon}{Commandes}$ </font>

Décompresser le fichier **Package-0.0.0.tar.gz**
    
        tar -xvzf Package-0.0.0.tar.gz
    
Puis installer le package **Package**
    
        python3 setup.py install

Enfin, se placer dans le dossier **Package**

        cd Package-0.0.0


Pour lancer les tests unitaires

        pytest test

<font size=7> $\color{maroon}{Contenu \space du \space package}$ </font>

- Deux fichiers **setup.py** et **setup.cfg** : essentiels pour configurer et installer proprement le package **Package**
- Ce fichier **README.md** : permet à l'utilisateur de comprendre le fonctionnement du package **Package**
- Un fichier **fuel2001.txt** : jeu de données inclu dans le package permettant de tester toutes les fonctionnalités du package 
- Un package **Package**
- Un package **test**

#### I - Fichier main

1- **La fonction lire :**

Cette fonction contenu dans le fichier main.py permet l'ouverture et la lecture des données. Le format initiale des donnée étant le CSV, il a fallu les importer sans l'utilisation de numpy et pandas.

**Entrée** : le fichier à lire

**Sortie** : une liste de liste contenant les données iniales avec la conversions de chaque ligne en son type correspondant (str en str, float, int en float)...
Le choix de convertir nos données en liste de liste s'explique par le fait que plus tard, on transformera nos données en matrice. Cela rend simple la manipulation.

2- En deuxième lieu, on extrait de notre dataset les données nécéssaire à la réalisation de notre regression. Pour cela, on nomme la matrice de données explicative ainsi que le vecteur des données à expliquer. L'extraction se fait via des fonction définies dans la class Matrix.

3- On réalise enfin le test des outils implémentés sur nos données.


#### II - Fichier mymodule1

L'implémentation de ce fichier découle du besoin de manipuler les données sans l'usage de librairies externes. Pour cela, il on a pensé à mettre en oeuvre une classe Matrix grâce aux outils de POO vus en cours. 

**La class Matrix **

1- Attribut: Elle admet uniquement comme attribut les donneées à transformer en type Matrix

2- Méthodes 

* **__init__**: propre à toute les classes, cette méthode défini ici les attributs dont on aura besoin. Elle se charge également de vérifier la nature des données à transformer en Matrix. On ne considère ici que deux types valides à savoir : les liste de liste ou les tuples de tuples. Autrement, une erreur est retournée à l'utilisateur.

* **get_size**: elle prend en entrée un objet de type  Matrix et retourne sa taille 

* **get_lines**: elle prend en entrée un objet de type  Matrix et retourne son nombre de ligne

* **get_col**: elle prend en entrée un objet de type  Matrix et retourne son nombre de colonne

* **__repr__**: il s'agit d'une super méthode, qui permet une représentation visuelle lorsqu'on appel tout objet de type Matrix. 

* **scalaire**: il s'agit d'une méthode dite statique. Elle n'a pas besoin d'un objet de type Matrix poir son fonctionnement. Elle prend en entrée deux vecteur et retourne leurs produits scalaire

* **copier**: égalemet une méthode statique, la méthode copier se charge d'effectuer une copie indépendante des données en entrée. Elle prends en entrée une liste de liste et retourne sa copie. On utilise pour cela la méthode **copy()** de python.

* **transpose**: cette méthode retourne la transposé d'une matrice. Elle prend en entrée un objet de type Matrix et retourne un objet de type Matrix.

* **__add__**: il s'agit d'une super méthode qui se charge d'additionner deux matrice. Elle prend en entrée deux objet de type Matrix et retourne un objet de type Matrix. On peut l'appeler via l'opérateur "+".

* **__mul__**: il s'agit d'une super méthode qui se charge d'effectuer un produit matriciel. Elle prend en entrée deux objet de type Matrix et retourne un objet de type Matrix. On peut l'appeler via l'opérateur "*".

* **__sub__**: il s'agit d'une super méthode qui se charge d'effectuer une soustraction matricielle. Elle prend en entrée deux objet de type Matrix et retourne un objet de type Matrix. On peut l'appeler via l'opérateur "-".

* **mat_id**: Cette méthode se charge de retourner une matrice identité. Elle prend en entrée un entier positif représentant la dimention de la matrice identité à créer et retourne un objet de type Matrix.

* **mineur**: il s'agit d'une méthode statique. Elle se charge de retourner la sous matrice correspondante en fonction des paramètres. Elle prends en entrée une liste de liste, un entier correspondant à la ligne à supprimer, un entier correspondant à la colonne à supprimer. Elle retourne un objet de type Matrix.

* **cofacteur**: Retourne le cofacteur (determinant de la sous matrice associée) en fonction des paramètres. Elle fait appelle à la méthode **déterminant**.Elle prend ene entrée un objet de type Matrix, un entier représentant la ligne à suprimer et un entier représentant la colonne à supprimer. Elle retourne un entier. 

* **determinant**: calcule le déterminant de la matrice en paramètre. Elle fait appelle à la méthode **cofacteur**. Prends un objet de type Matrrix et retourne un entier.

* **comatrice**: calcule la comatrice (matrice des cofacteurs) associée à la matrice en paramètre. Elle fait appelle à la méthode **cofacteur**. Elle prend en entrée un objet de type Matrix et retourne un objet de type Matrix.

* **inverse**: calcule l'inverse de la matrice en paramètre. Elle fait appelle à la méthode **comatrice**, **determinant** et **transpose**. Elle prends en entrée un objet de type Matrix er retourne un objet de type Matrix.

* **puissance** : calcule la puissance n de tous les éléments d'une matrice. Elle prends en entrée un objet de type Matrix ainsi qu'un entier représentant la puissance. Elle retourne un objet de type Matrix.

* **supcol**: cette méthode se charge de suprimer une colonne de la matrice en paramètre. Elle prends en entrée un objet de type Matrix ainsi qu'un entier correspondant au numéro de la colonne à supprimer. Elle ne retourne rien.

* **supligne**: cette méthode se charge de suprimer une ligne de la matrice en paramètre. Elle prends en entrée un objet de type Matrix ainsi qu'un entier correspondant au numéro de la ligne à supprimer. Elle ne retourne rien.

* **addcol**: elle ajoute une colonne à la matrice en paramètre. Elle prends en entrée un objet de type Matrix, une liste correspondant à la colonne à ajouter et un entier qui représente la position de la nouvelle colonne. Elle ne retourne rien.

* **addligne**: elle ajoute une ligne à la matrice en paramètre. Elle prends en entrée un objet de type Matrix, une liste correspondant à la ligne à ajouter et un entier qui représente la position de la nouvelle ligne. Elle ne retourne rien 

* **getcol**: cette méthode extrait une colonne de la matrice en paramètre. Elle prends en entrée un objet de type matrix, un entier correspondant au numéro de la colonne à extraire. Elle retourne une liste.

* **getligne**: cette méthode extrait une ligne de la matrice en paramètre. Elle prends en entrée un objet de type matrix, un entier correspondant au numéro de la ligne à extraire. Elle retourne une liste.

#### III - Fichier mymodule2

Dans ce fichier, on va à présent implémenter les régressions (moindres carrée ordinaires et Ridge). On aura besoin de la librairie matplotlib pour la visualisation.

1- **Class LinearModel**

Il s'agit de la classe partagée par toutes les régressions linéaires en générale. C'est donc une classe mère dont nos deux autres classes hériterons.

- Elle admet pour seul attribut intercept qui est un booléen. Il prends la valeur "True" quand la constante fait partit du modèle et "False" sinon.

- Les méthodes

  - **predict**: prend des données de test Xt et renvoie les prédictions associées.
  - **get_coeffs**: retourne les valeurs des coefficients estimés
  - **determination_coefficient**: calcule et renvoie le coefficient R^2
  - **interval_conf** : calcule et retourne un interval de confiance pour chaque beta
  - **visualisation**: permet la visualisation des valeurs prédites et des valeurs observées
  
2- **Class OrdinaryLeasSquares**

On implémente ici l'estimateur des moindres carrés ordinaires. C'est une classe fille de LinearModel

- Elle admet pour seul attribut intercept qui est un booléen. Il prends la valeur "True" quand la constante fait partit du modèle et "False" sinon.

- Elle admet également une seule méthode qu'est **fit**. Cette méthode prend des données X et y en entrée et calcule l’estimateur des moindres carrés $\beta$
  
3- **Ridge**

On implémente ici l'estimateur de ridge. C'est une classe fille de LinearModel

- Les attributs

  - **intercept** qui est un booléen. Il prends la valeur "True" quand la constante fait partit du modèle et "False" sinon.
  
  - **param** qui représente le paramètre lambda de la regression de ridge
  
- La seule méthode de cette classe est **fit** qui prend des données $X$ et $y$ en entrée et calcule l’estimateur de ridge $\beta$
  
