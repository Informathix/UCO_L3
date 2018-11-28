::: {.header}
::: {.header_interior}
\
:::

::: {.content_body}
::: {.content_interior}
::: {.left_column}
\

::: {.navigation}
-   [Courbes](#exo1)
-   [Intégrale](#exo2)
-   [Camembert](#exo3)
-   [Histogramme](#exo4)
-   [Image](#exo5)
-   [3D](#exo6)
-   [Help!](#help)
:::

::: {.navigationbtm}
:::

\
:::

::: {.right_column}
matplotlib en action
====================

::: {.endright_column2}
\
![matplotlib](images/logo-matplotlib.png "matplotlib"){width="250"}
:::

Ci-dessous quelques exercices pour apprendre à jouer avec matplotlib et
numpy. Ils sont à peu près par ordre croissant de difficulté, mais ils
peuvent être faits indépendamment les uns des autres.

\
\

#### [Mon premier cosinus]{#exo1}

::: {.endright_column2}
\
[![cosinus](images/cos.png "cosinus"){width="150"}](images/cos.png)
:::

Dans cet exercice, nous allons tracer les fonctions sinus et cosinus.
Voici la recette inratable :

-   Commencer par importer *numpy* et *matplotlib.pyplot*.
-   Utiliser la fonction
    [linspace](http://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html)
    de numpy pour définir les valeurs de *x*. On se restreindra à
    l\'intervalle *\[-π;π\]*.
-   Utiliser la fonction
    [plot](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot)
    de matplotlib pour tracer la courbe en trait plein rouge. La
    fonction
    [sinus](http://docs.scipy.org/doc/numpy/reference/generated/numpy.sin.html)
    est définie dans numpy.
-   Utiliser la fonction
    [show](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.show)
    de matplotlib pour admirer le résultat en exécutant le code.
-   Jouer sur l\'argument *num* de la fonction *linspace*. Observer.
    Pour la suite, on pourra prendre *100* pour ce paramètre.
-   De manière similaire, tracer la fonction cosinus en bleu.
-   Mettre la légende dans le coin en haut à gauche en utilisant la
    fonction
    [legend](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.legend).
-   Ajouter un titre aux deux axes en utilisant les fonctions
    [xlabel](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.xlabel)
    et
    [ylabel](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.ylabel).
-   Fixer les limites de chaque axe en utilisant la fonction
    [axis](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.axis)
    de matplotlib.
-   Indiquer sur la figure des valeurs -1, 0 et 1 sur l\'axe des *y* à
    l\'aide de la fonction
    [yticks](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.yticks).
-   De même, indiquer sur l\'axe des *x* les valeurs -π, -π/2, 0, π/2 et
    π en utilisant la fonction
    [xticks](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.xticks).
    On pourra pour cela utiliser le parser latex de matplotlib (voir
    [ici](http://matplotlib.org/users/usetex.html)).
-   Ajouter de discrètes lignes verticales et horizontales en face des
    valeurs indiquées sur les deux axes à l\'aide de la fonction
    [grid](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.grid).
-   Enfin, utiliser la fonction
    [savefig](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.savefig)
    pour sauvegarder automatiquement la figure produite au format *png*.

\
\
\

#### [Ma première intégrale]{#exo2}

::: {.endright_column2}
\
[![integrale](images/integrale.png "integrale"){width="150"}](images/integrale.png)
:::

Dans cet exercice, nous allons dessiner une courbe et montrer son
intégration sur un intervalle comme étant l\'aire sous la courbe

Définir la fonction *f(x) = (x - 3) \* (x - 5) \* (x - 7) + 85*. Tracer
cette fonction sur l\'intervalle \[0; 10\] en faisant commencer l\'axe
des *y* à 0 à l\'aide de la fonction
[ylim](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.ylim).

On va intégrer entre *a = 2* et *b = 9*. Définir *a* et *b* et les
indiquer sur l\'axe des *x* en utilisant la fonction
[xticks](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.xticks).
Utiliser la fonction
[yticks](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.yticks)
pour enlever toutes les valeurs de l\'axe y. Enfin, utiliser la fonction
[tick\_params](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.tick_params)
pour enlever les deux \'ticks\' sur l\'axe du haut.

Utiliser la fonction
[figtext](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.figtext)
pour indiquer \'x\' en bas à droite sous l\'axe des *x* et \'y\' en haut
à gauche de l\'axe des *y*.

Utiliser la fonction
[subplots](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.subplots)
pour créer un *subplot* (qui va contenir notre figure) et stocker les
valeurs de retour de cette fonction.

Définir *x2* comme étant dans l\'intervale \[a; b\] en utilisant la
fonction
[linspace](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.linspace).
Définir *y2* comme étant les valeurs de f(x2).

Importer la fonction
[Polygon](http://matplotlib.org/api/patches_api.html#matplotlib.patches.Polygon)
de matplotlib.patches qui va nous permettre de dessiner des polygones
(nécessaires pour dessiner des surfaces).
[add\_patch](http://matplotlib.org/1.4.0/api/axes_api.html?highlight=add_patch#matplotlib.axes.Axes.add_patch)
pour ajouter le polygone que l\'on va créer à notre figure

Le premier argument de la fonction Polygon est un tableau de taille N\*2
qui indique les coordonnées des sommets du polygone. Utiliser les
fonctions python
[zip](https://docs.python.org/3/library/functions.html?highlight=zip#zip)
et [list](https://docs.python.org/3/library/stdtypes.html#list) pour
mettre les coordonnées *x2* et *y2* au bon format pour la fonction
Polygon. Utiliser 0.9 comme valeur pour le paramètre *facecolor* et 0.5
pour le paramètre *edgecolor*.

Utiliser la fonction
[text](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.text)
pour afficher la formule de l\'intégrale au milieu du polygone. Puis
sauvegarder l\'image au format pdf.

\
\
\

#### [Mon premier camembert]{#exo3}

::: {.endright_column2}
\
[![camembert](images/camembert.png "camembert"){width="150"}](images/camembert.png)
:::

Dans cet exercice, nous allons réaliser un camembert pour représenter la
répartition suivante entre 5 options : option 1 = 25; option 2 = 15;
option 3 = 60; option 4 = 30 et option 5 = 14.

Pour cela, nous allons utiliser la fonction
[pie](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.pie)
de matplotlib.

Utiliser la propriété *equal* dans la fonction
[axis](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.axis)
pour que le camembert soit circulaire.

Définir les couleurs des 5 parts en utilisant les couleurs html :
*lightseagreen*, *lightsalmon*, *lightskyblue*, *lightcoral* et
*lightgreen*.

Utiliser l\'attribut *autopct* pour afficher les pourcentages à
l\'intérieur de chaque part.

Utiliser l\'attribut *explode* pour faire ressortir les résultats de
l\'option 2 et de l\'option 4.

Jouer avec les attributs *counterclock* et *startangle*. Observer.

Modifier l\'attribut *textprops* pour mettre le texte en gras et le
grossir.

Au lieu de mettre en dur dans le code les valeurs pour chaque option, on
va utiliser un fichier externe *donnees.txt* qui stockera ces valeurs
(et qui pourra avoir été généré par un autre programme). Ensuite, on
accèdera aux données de ce fichier en utilisant la fonction
[loadtxt](http://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html)
de numpy.

\
\
\

#### [Mon premier histogramme]{#exo4}

::: {.endright_column2}
\
[![histogramme](images/histo.png "histogramme"){width="150"}](images/histo.png)
:::

Dans cet exercice, nous allons tracer des histogrammes de répartition
des notes à des devoirs, notes générées aléatoirement en utilisant des
lois bien connues.

Pour générer les notes des 26 étudiants aux 4 devoirs, nous allons
utiliser les lois de probabilité du module
[random](http://docs.scipy.org/doc/numpy/reference/routines.random.html)
de numpy. On pourra par exemple utiliser une loi uniforme pour le
premier devoir, une loi de puissance pour le deuxième (c\'était un
devoir à la maison), une loi de Poisson pour le troisième et une loi de
Laplace pour le quatrième. Les paramètres de ces lois sont laissées à la
discrétion des participants. On pourra utiliser la fonction
[round](https://docs.python.org/3/library/functions.html?highlight=round#round)
pour arrondir les notes à 2 chiffres après la virgule.

Nous allons maintenant utiliser la fonction
[hist](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.hist)
pour tracer les histogrammes correspondants à chaque devoir. On pourra
utiliser le type *bar* et fixer le paramètre *alpha* à 0.8 pour que les
barres soient légèrement transparentes.

Observer l\'axe des x et faire quelque chose pour qu\'il indique ce
qu\'on s\'attend à voir.

Avoir les quatres histogrammes sur la même figure n\'est pas très
lisible. Nous allons donc les mettre chacun dans une sous-figure
différente à l\'aide de la commande
[subplots](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.subplots).
Modifier le reste du script pour que ça marche comme on veut.

On va maintenant rajouter un cinquième histogramme qui va contenir les
moyennes de chaque devoir et l\'écart-type. Pour cela, au lieu
d\'utiliser la fonction *subplots*, on va utiliser la fonction
[subplot2grid](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.subplot2grid)
pour que le dernier histogramme prenne toute la largeur de la figure.
Pour dessiner cet histogramme, on utilisera la fonction
[bar](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.bar).
Pour calculer les moyennes et les écarts-types, on utilisera les
fonctions numpy
[mean](http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html)
et
[std](http://docs.scipy.org/doc/numpy/reference/generated/numpy.std.html).

\
\
\

#### [Ma première image]{#exo5}

::: {.endright_column2}
\
[![histogramme](images/GH-image.png "histogramme"){width="150"}](images/GH-image.png)
:::

Dans cet exercice, on va manipuler une image et tracer les histogrammes
des RVB : un histogramme représentant la répartition entre les
différentes valeurs possibles pour chacune des 3 couleurs de base
(rouge, vert, bleu).

Commençons par télécharger l\'image png qui se trouve
[là](images/Grace_Hopper.png). Ensuite, il faut importer l\'image dans
matplotlib grâce à la fonction
[imread](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.imread)
puis afficher l\'image avec la fonction
[imshow](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.imshow).
Noter que, comme expliqué
[ici](http://matplotlib.org/users/image_tutorial.html), *imread* renvoie
un tableau contenant les valeurs RVB pour chaque pixel.

Utiliser la fonction
[axis](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.axis)
pour enlever les axes *x* et *y*.

Utiliser la fonction
[axes](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.axes)
pour positionner 4 sous-figures, une au-dessus, une à droite, une
en-dessous et une à gauche, en indiquant leurs coordonnées dans la
figure globale (paramètre *rect*).

Remplir 3 des sous-figures crées avec les 3 histogrammes de couleur en
utilisant la fonction
[hist](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.hist)
avec *stepfilled* comme valeur pour le paramètre *histtype*. Utiliser la
dernière sous-figure pour tracer l\'histogramme de la luminosité de
l\'image (valeurs cumulées pour les trois couleurs).

Utiliser les fonctions appropriées pour ajouter une légende à chaque
graphe, ajouter des valeurs sur les axes et enlever celles qui sont
illisibles.

\
\
\

#### [Mon premier 3D]{#exo6}

::: {.endright_column2}
\
[![3D](images/3d.png "3D"){width="150"}](images/3d.png)
:::

Dans cet exercice, nous allons tracer une courbe en 3D, la projeter et
la faire tourner.

Tout d\'abord, nous allons utiliser la fonction
[gca](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.gca)
pour créer une figure 3D en fixant le paramètre *projection* à *3d*.

Ensuite, nous allons utiliser la classe
[axes3d](http://matplotlib.org/mpl_toolkits/mplot3d/api.html#axes3d) du
module *mplot3d* de *mpl\_toolkits* (un module de matplotlib). Nous
allons utiliser la fonction
[get\_test\_data](http://matplotlib.org/mpl_toolkits/mplot3d/api.html#module-mpl_toolkits.mplot3d.axes3d)
pour générer les données.

Pour tracer la courbe 3D, nous allons utiliser la fonction
[plot\_surface](http://matplotlib.org/1.3.1/mpl_toolkits/mplot3d/tutorial.html#surface-plots)
du module *mplot3d*. On utilisera 8 comme valeur pour les paramètres
*rstride* et *cstride* et 0.3 pour *alpha*.

Utiliser la fonction
[contourf](http://matplotlib.org/1.3.1/mpl_toolkits/mplot3d/tutorial.html#filled-contour-plots)
du module *mplot3d* pour projeter la courbe sur les trois plans. Lancer
le script et faire tourner la courbe!

\
\
\

#### [Où trouver de l\'aide]{#help}

-   [La référence numpy](http://docs.scipy.org/doc/numpy/reference/)
    (en)
-   [matplotlib](http://matplotlib.org) (en)
-   [gallerie matplotlib](http://matplotlib.org/gallery.html) (en)
-   [un tutoriel sur les images en
    matplotlib](http://matplotlib.org/users/image_tutorial.html) (en)
-   [une introduction à
    matplotlib](http://www.science-emergence.com/Matplotlib/) (fr)
-   [l\'article Wikipédia sur
    matplotlib](http://en.wikipedia.org/wiki/Matplotlib) (en) avec
    quelques exemples
-   [une introduction à
    numpy/scipy/matplotlib](http://math.mad.free.fr/depot/numpy/essai.html)
    (fr)
:::
:::

\
:::

::: {.footer}
::: {.footer-inner}
::: {.footer-div}
[![Valid XHTML 1.0
Strict](http://www.w3.org/Icons/valid-xhtml10-blue){width="88"
height="31"}](http://validator.w3.org/) [![Valid CSS
Strict](http://www.w3.org/Icons/valid-css2-blue){width="88"
height="31"}](http://jigsaw.w3.org/css-validator/)
:::

------------------------------------------------------------------------

::: {style="text-align:center;"}
Copyright © 2014 Anne-Cécile Orgerie
:::
:::
:::
:::
