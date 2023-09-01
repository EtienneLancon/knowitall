[Retour au sommaire](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/sommaire.md)

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
Inversement, si pour tout $n$, $u_n < u_n-1$, la suite est dite **décroissante**.

## Représentation graphique

La représentation graphique d'une suite numérique est une suite de points dont les abscisses sont les entiers naturels $n$ et les ordonnées les valeurs des termes $u_n$.

Si les termes de la suite peuvent se rapprocher indéfiniment d'une valeur $l$, on dit que $l$ est la **limite** de la suite en $+\infty$.

> On note alors $\lim\limits_{n \to +\infty} u_n = l$

$l$ n'est pas forcément un nombre réel. $+\infty$, $-\infty$ sont des limites possibles.

![fig_01](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/002_suites_numeriques/ressources/002_fig_01.png)

## Suites arithmétiques

> [!WARNING]  
> Formules à retenir par coeur

Une suite arithmétique est une suite dont les termes $u_n$ sont définis par la relation de récurrence :  

$u_{n+1} = u_n + r$

$r$ étant un nombre réel appelé **raison** de la suite.

Si $r$ est positif, la suite est croissante.  
Si $r$ est négatif, la suite est décroissante.

On peut aussi définir un terme quelconque d'une suite arithmétique comme étant le nombre de fois que la raison $r$ est ajoutée au terme initial $u_0$ :

$u_n = u_0 + nr$

On peut étendre cette formule à deux termes quelconques qui auront alors pour différence la raison $r$ multipliée par le nombre de termes qui les séparent :

$u_n = u_p + (n-p)r$

### Somme des termes d'une suite arithmétique

La somme des termes de $u_0$ à $u_n$, notée $S_n$, d'une suite arithmétique est égale à la moyenne des termes extrêmes multipliée par le nombre de termes.

La moyenne des termes extrêmes est égale à la moyenne du premier et du dernier terme, soit $\frac{u_0 + u_n}{2}$.

Le nombre de termes est égal à $n+1$.  
On a donc :
$$S_n = \frac{{\color{teal}u_0 + u_n}}{2} \times (n+1)$$


Comme les fois précédentes, on peut étendre cette formule à deux termes quelconques :

$$\sum_p^n = \frac{u_p + u_n}{2} \times (n-p+1)$$

> Pour ceux qui ne seraient pas accoutumés à ce symbole, il signifie "la somme des termes de $u_p$ à $u_n$".

Un petit schéma un peu (très) simpliste pour illustrer la problématique de manière intuitive :

![fig_02](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/002_suites_numeriques/ressources/002_fig_02.png)

La droite en pointillés rouges étant ${\color{teal}u_0 + u_n}$, y'a quelque chose de divisé par deux qui se balade par ici, vous en conviendrez.

Un petit rappel de géométrie au passage :  
L'aire d'un rectangle est égale à la longueur multipliée par la largeur.  
L'aire d'un triangle est égale à la longueur multipliée par la largeur, _le tout divisé par deux_.

>C'est une approche très intuitive, mais qui ne constitue pas une démonstration, et qui ne peut pas être considérée comme une preuve.  
>De plus il ne faut pas croire que toutes les suites arithmétiques forment un triangle avec l'axe des abcisses.

Pour une démonstration plus rigoureuse, je vous encourage à consulter [cette page](https://les-suites.fr/arithmetique/somme-des-termes.php).



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

Le **sens de variation** de la suite dépend des valeurs de $q$ et $u_0$.

Si $u_0 > 0$ :  
- Si $q > 1$, la suite est croissante.  
- Si $0 < q < 1$, la suite est décroissante.

Si $u_0 < 0$ :
- Si $q > 1$, la suite est décroissante.
- Si $0 < q < 1$, la suite est croissante.

On note que le cas $q < 0$ n'est pas mentionné car on ne poura alors pas définir de sens de variation, chaque terme de la suite étant de signe opposé au précédent.

### Somme des termes d'une suite géométrique

La somme des termes de $u_0$ à $u_n$, notée $S_n$, d'une suite géométrique est égale à la formule suivante :

$$S_n = u_0 \times \frac{1-q^{n}}{1-q}$$


*Comprendre cette formule*

Dans le cas d'une raison $q$ telle que $0 < q < 1$, plus $n$ est grand, plus $q^n$ est petit, et donc plus $u_n$ est petit.

![fig_03](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/002_suites_numeriques/ressources/002_fig_03.png)

Ainsi la majeure partie de la somme des termes de la suite sera constituée des premiers termes, qui sont les plus grands.

**A l'inverse**, dans le cas d'une raison $q$ telle que $q > 1$, plus $n$ est grand, plus $q^n$ est grand, et donc plus $u_n$ est grand.

![fig_04](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/002_suites_numeriques/ressources/002_fig_04.png)

Dans ce cas, c'est les premiers termes qui sont les plus petits, et la majeure partie de la somme des termes de la suite sera constituée des derniers termes, qui sont les plus grands.

Le but de cette formule est de prendre en compte de manière naturelle la valeur de $u_0$ en la multipliant par une valeur, $\frac{1-q^{n}}{1-q}$, qui ne sera jamais inférieure à 1 pour garantir l'intégrité de $u_0$, et qui d'une part   
- Sera très légèrement supérieure à 1 si $q < 1$
- Aura une valeur exponentielle selon $n$ si $q > 1$.

Une fois de plus je vous invite à aller voir la démonstration sur [cette page](https://les-suites.fr/geometrique/somme-des-termes.php).

Comme à chacune des formules, on peut l'étendre à deux termes quelconques :

$$\sum_p^n = u_p \times \frac{1-q^{n-p+1}}{1-q}$$

[Retour au sommaire](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/sommaire.md)