# Suites numériques

## Définition

Une suite numérique est une fonction restreinte aux seuls entiers naturels $\mathbb{N}$.  
La suite peut être définie sur un intervalle $[a;b]$ ou sur tout $\mathbb{N}$.  

Une suite numérique est notée $(u(n))$ ou $(u_n)$.  
Elle peut être définie par une formule explicite, ou par une relation de récurrence. 

Un **terme** noté $u_n$ désigne l'image de $n$ au travers de la suite $(u_n)$.

Dans le cas d'une formule explicite, $u_n$ est exprimé selon $\color{orange}n$.  
Dans le cas d'une relation de récurrence, $u_n$ est exprimé selon $\color{orange}u_{n-1}$.  
Lorsque la valeur de $u_n$ dépend de $u_{n-1}$, il est nécessaire que la suite aie un **terme initial** $u_0$ dont la valeur déterminera celle de tous les autres termes de la suite.

Exemple de suite définie par une formule explicite :

$u_n = 2{\color{orange}n}+1$

Exemple de suite définie par une relation de récurrence :

$u_n = {\color{orange}u_{n-1}} + 2$



Si pour tout $n$, $u_n > u_n-1$, la suite est dite **croissante**.  
Inversement, si pour tous $n$, $u_n < $u_n-1$, la suite est dite **décroissante**.

## Représentation graphique

La représentation graphique d'une suite numérique est une suite de points dont les abscisses sont les entiers naturels $n$ et les ordonnées les valeurs des termes $u_n$.

Si les termes de la suite peuvent se rapprocher indéfiniment d'une valeur $l$, on dit que $l$ est la **limite** de la suite en $+\infty$.

> On note alors $\lim\limits_{n \to +\infty} u_n = l$

$l$ n'est pas forcément un nombre réel. $+\infty$, $-\infty$ sont des limites possibles.

![fig_02](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/002_suites_numeriques/ressources/002_fig_01.png)

## Suites arithmétiques

> [!WARNING]  
> Formules à retenir par coeur

Une suite arithmétique est une suite dont les termes $u_n$ sont définis par la relation de récurrence :  

$u_{n+1} = u_n + r$

$r$ étant un nombre réel appelé **raison** de la suite.

On peut aussi définir une suite arithétique comme étant le nombre de fois que la raison $r$ est ajoutée à un terme initial $u_0$ :

$u_n = u_0 + nr$

On peut étendre cette formule à deux termes quelconques qui auront alors pour différence la raison $r$ multipliée par le nombre de termes qui les séparent :

$u_n = u_p + (n-p)r$

Si $r$ est positif, la suite est croissante.  
Si $r$ est négatif, la suite est décroissante.

### Somme des termes d'une suite arithmétique



## Suites géométriques

> [!WARNING]  
> Formules à retenir par coeur

Une suite géométrique est une suite dont les termes $u_n$ sont définis par la relation de récurrence :

$u_{n+1} = u_n \times q$

$q$ étant un nombre réel appelé **raison** de la suite, noté $q$ car il est le quotient entre deux termes consécutifs.

Tout comme les suites arithmétiques, on peut définir une suite géométrique comme étant le nombre de fois que la raison $q$ est multipliée à un terme initial $u_0$ :

$u_n = u_0 \times q^n$

Et l'on peut de même élargir à

$u_n = u_p \times q^{n-p}$