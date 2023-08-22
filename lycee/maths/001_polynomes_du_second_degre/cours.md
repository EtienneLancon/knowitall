# Fonctions pôlynomes du second degré

On appelle pôlynome du second degré une fonction du type

$f(x)=ax²+bx+c$

Où a, b et c sont des nombres réel et où **a est non nul**. 
Si a est nul alors la fonction $f$ est une fonction affine.

## Représentation graphique

La courbe d'un pôlynome est une **parabole**.  
Lorsque x tend vers $+\infty$ et $-\infty$, $f$(x) peut tendre vers $+\infty$ ou $-\infty$.  
En langage barbare, lorsque x tend vers la gauche et la droite, $f$(x) peut tendre vers le haut ou vers le bas.  
Nous verrons plus tard comment déterminer cela par calcul avec un tableau de signes.  


### Intersection avec l'axe des abscisses

Si la fonction $f$ possède un minimum **inférieur à 0** et tend vers $+\infty$ OU si elle possède un maximum **supérieur à 0** et tend vers $-\infty$, alors elle croisera l'axe des abscisses en deux points $x_1$ et $x_2$.  
![fig_001](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/001_polynomes_du_second_degre/ressources/001_fig_01.png)
![fig_002](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/001_polynomes_du_second_degre/ressources/001_fig_02.png)

### Contact avec l'axe des abscisses

Si elle possède un minimum / maximum égal à 0 alors elle ne "touchera" l'axe des abscisses qu'en un seul point qu'on nommera $x_0$.  

![fig_003](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/001_polynomes_du_second_degre/ressources/001_fig_03.png)

### Absence de contact avec l'axe des abscisses

Si elle possède un minimum **supérieur à 0** et tend vers $+\infty$ OU si elle possède un maximum **inférieur à 0** et tend vers $-\infty$, alors elle ne croisera pas l'axe des abscisses.

![fig_004](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/001_polynomes_du_second_degre/ressources/001_fig_04.png)
![fig_005](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/001_polynomes_du_second_degre/ressources/001_fig_05.png)

On nomme ces valeurs d'interaction entre la courbe du pôlynome et l'axe des abcisses $x_1$ et $x_2$ / $x_0$ les **racines du pôlynome**.  
Ce sont les valeurs de $x$ pour lesquelles $f(x) = 0$;


## Calcul des racines du pôlynome

Calculer les racines du pôlynome revient donc à trouver par calcul les valeurs de x pour lesquelles la fonction f(x) vaudra 0.
On a vu dans la partie [représentation graphique](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/001_polynomes_du_second_degre/cours.md#repr%C3%A9sentation-graphique) que cette question avait parfois 2 réponses, parfois 1, et parfois pas de réponse.

Pour savoir dans quel cas l'on se trouve, on calcule en premier lieu le **discriminant** delta.

$\Delta = b² -4ac$

Si $\Delta = 0$ on a une réponse ([un contact avec les abscisses](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/001_polynomes_du_second_degre/cours.md#contact-avec-laxe-des-abscisses))  
Et l'on peut trouver la racine grâce à la formule  $x_0 = \frac{-b}{2a}$ 

Si $\Delta > 0$ on a deux réponses ([deux intersections avec les abscisses](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/001_polynomes_du_second_degre/cours.md#intersection-avec-laxe-des-abscisses))  
Et l'on a  
$x_1 = \frac{-b-\sqrt{\Delta}}{2a}$  

$x_2 = \frac{-b+\sqrt{\Delta}}{2a}$

Si $\Delta < 0$ on a pas de réponse ([pas de contact avec les abscisses](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/001_polynomes_du_second_degre/cours.md#absence-de-contact-avec-laxe-des-abscisses))


## Formes d'un pôlynome
La fonction pôlynome $f$ peut être écrite de plusieurs manières, ou **formes**.

**Forme développée**

$f(x)=ax²+bx+c$

**Forme factorisée**

Si $\Delta > 0$ alors

$f(x)=a(x-x_1)(x-x_2)$

Si $\Delta = 0$ alors

$f(x)=a(x-x_0)²$

Si $\Delta < 0$ alors $f$ n'a pas de forme factorisée

**Forme canonique**

$f(x)=a(x-\alpha)²+\beta$

Où 

$\alpha = \frac{-b}{2a}$


$\beta = \frac{\Delta}{4a} = \frac{b²-4ac}{4a}$

## Etude du signe d'un pôlynome

Etudier le signe d'un pôlynome revient à se demander "pour chaque $x$, est-ce que $f(x)$ est positif ou négatif ?", autrement dit, pour chacune des valeurs, est-ce que ma courbe est au-dessus ou en dessous de l'axe des abscisses ?

Dans le cas où le pôlynome est sous forme factorisée, on peut utiliser le tableau de signes pour trouver les valeurs de $x$ pour lesquelles $f(x)$ est positif ou négatif.

Pour $\Delta > 0$ on a

Todo: tableau de signes

Pour $\Delta = 0$ on a

Todo: tableau de signes

Pour $\Delta < 0$ on a

Todo: tableau de signes

> [!IMPORTANT]  
> Prenez le temps de bien comprendre la relation entre ces tableaux de signes, les [représentations graphiques](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/001_polynomes_du_second_degre/cours.md#repr%C3%A9sentation-graphique) et [la valeur du discriminant](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/001_polynomes_du_second_degre/cours.md#calcul-des-racines-du-p%C3%B4lynome).