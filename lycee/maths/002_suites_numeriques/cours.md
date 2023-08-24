# Suites numériques

## Définition

Une suite numérique est une fonction restreinte aux seuls entiers naturels $\mathbb{N}$.  
La suite peut être définie sur un intervalle $[a;b]$ ou sur tout $\mathbb{N}$.  

Une suite numérique est notée $(u(n))$ ou $(u_n)$.  
Elle peut être définie par une formule explicite, ou par une relation de récurrence. 

Un **terme** noté $u_n$ désigne l'image de $n$ au travers de la suite $(u_n)$.

Dans le cas d'une formule explicite, $u_n$ est exprimé selon $\color{orange}n$.  
Dans le cas d'une relation de récurrence, $u_n$ est exprimé selon $\color{orange}u_{n-1}$.

Exemple de suite définie par une formule explicite :

$u_n = 2{\color{orange}n}+1$

Exemple de suite définie par une relation de récurrence :

$u_n = {\color{orange}u_{n-1}} + 2$

Lorsque comme ici la valeur de $u_n$ dépend de $u_{n-1}$, il est nécessaire que la suite aie un **terme initial** $u_0$ dont la valeur déterminera celle de tous les autres termes de la suite.

## Représentation graphique

La représentation graphique d'une suite numérique est une suite de points dont les abscisses sont les entiers naturels $n$ et les ordonnées les valeurs des termes $u_n$.

Si les termes de la suite peuvent se rapprocher indéfiniment d'une valeur $l$, on dit que $l$ est la **limite** de la suite en $+\infty$.

> On note alors $\lim\limits_{n \to +\infty} u_n = l$

$l$ n'est pas forcément un nombre réel. $+\infty$, $-\infty$ sont des limites possibles.