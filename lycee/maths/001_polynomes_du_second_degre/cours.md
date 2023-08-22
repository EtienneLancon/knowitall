# Fonctions pôlynomes du second degré

On appelle pôlynome du second degré une fonction du type

$f(x)=ax²+bx+c$

Où a, b et c sont des nombres réel et où **a est non nul**. 
Si a est nul alors la fonction f est une fonction affine.

## Représentation graphique

La courbe d'un pôlynome est une **parabole**.  
Lorsque x tend vers $+\infty$ et $-\infty$, f(x) peut tendre vers $+\infty$ ou $-\infty$.  
En langage barbare, lorsque x tend vers la gauche et la droite, f(x) peut tendre vers le haut ou vers le bas.  
Nous verrons plus tard comment déterminer cela par calcul avec un tableau de signes.  


### Intersection avec l'axe des abscisses

Si elle possède un minimum **inférieur à 0** et tend vers $+\infty$ OU si elle possède un maximum **supérieur à 0** et tend vers $-\infty$, alors elle croisera l'axe des abscisses en deux points $x_1$ et $x_2$.  
![fig_001](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/001_polynomes_du_second_degre/ressources/001_fig_01.png)
![fig_002](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/001_polynomes_du_second_degre/ressources/001_fig_02.png)

### Absence de contact avec l'axe des abscisses

Si elle possède un minimum / maximum égal à 0 alors elle ne "touchera" l'axe des abscisses qu'en un seul point qu'on nommera $x_0$.  

![fig_003](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/001_polynomes_du_second_degre/ressources/001_fig_03.png)

Si elle possède un minimum **supérieur à 0** et tend vers $+\infty$ OU si elle possède un maximum **inférieur à 0** et tend vers $-\infty$, alors elle ne croisera pas l'axe des abscisses.

![fig_004](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/001_polynomes_du_second_degre/ressources/001_fig_04.png)
![fig_005](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/001_polynomes_du_second_degre/ressources/001_fig_05.png)

On nomme ces valeurs $x_1$ et $x_2$ / $x_0$ les **racines du pôlynome**.  
Ce sont les valeurs de x pour lesquelles f(x) = 0;  
Nous verrons [plus tard](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/001_polynomes_du_second_degre/cours.md#calcul-des-racines-du-p%C3%B4lynome) comment les déterminer par calcul.


## Formes d'un pôlynome
Le pôlynome f peut être écrit de plusieurs manières, ou **formes**.

**Forme développée**

$f(x)=ax²+bx+c$

**Forme factorisée**

$f(x)=a(x-x_1)(x-x_2)$

Où $x_1$ et $x_2$ sont les racines du pôlynome.

**Forme canonique**

$f(x)=a(x-\alpha)²+\beta$

Zen, roule tranquille, on voit plus loin $\alpha$ (alpha) et $\beta$ (beta)

## Calcul des racines du pôlynome

Calculer les racines du pôlynome revient donc à trouver par calcul les valeurs de x pour lesquelles la fonction f(x) vaudra 0.
On a vu dans la partie précédente [représentation graphique](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/001_polynomes_du_second_degre/cours.md#repr%C3%A9sentation-graphique) que cette question avait parfois 2 réponses, parfois 1, et parfois pas de réponse.

Pour savoir dans quel cas l'on se trouve, on calcule en premier lieu le **discriminant** delta.

$\Delta  = b² -4ac$

Si $\Delta > 0$ on a deux réponses (deux intersections avec les abscisses)  
Si $\Delta = 0$ on a une réponse (un contact avec les abscisses)  
Si $\Delta < 0$ on a pas de réponse (pas de contact avec les abscisses)
