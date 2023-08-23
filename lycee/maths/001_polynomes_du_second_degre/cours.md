# Fonctions pôlynomes du second degré

On appelle pôlynome du second degré une fonction du type

$f(x)=ax²+bx+c$

Où a, b et c sont des nombres réel et où **a est non nul**. 
Si a est nul alors la fonction $f$ est une fonction affine.

Exemple de pôlynome du second degré : $f(x)=2x²+3x-1$

Avec a = 2, b = 3 et c = -1

## Représentation graphique

La courbe d'un pôlynome est une **parabole**.  
Lorsque x tend vers $+\infty$ et $-\infty$, $f$(x) peut tendre vers $+\infty$ ou $-\infty$.  
En langage barbare, lorsque x tend vers la gauche et la droite, $f$(x) peut tendre vers le haut ou vers le bas.  
Nous verrons plus tard comment déterminer cela par calcul avec un [tableau de signes](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/001_polynomes_du_second_degre/cours.md#etude-du-signe-dun-p%C3%B4lynome).  


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

> [!WARNING]  
> Formules à retenir par coeur

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

## Formes d'un pôlynome
La fonction pôlynome $f$ peut être écrite de plusieurs manières, ou **formes**.

> [!WARNING]  
> Formules à retenir par coeur

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


$\beta = -\frac{\Delta}{4a} = -(\frac{b²-4ac}{4a})$


## Passage d'une forme à l'autre

> [!INFO]
> L'important ici n'est pas de retenir par coeur mais de comprendre comment passer d'une forme à l'autre en jouant avec a, b et c.

### Forme développée vers forme factorisée

On utilise la formule du discriminant pour trouver les racines du pôlynome $x_1$ et $x_2$ ou $x_0$.

Si $\Delta = 0$ alors $x_0 = \frac{-b}{2a}$ 

$$ax²+bx+c = a(x-{\color{teal}x_0})²$$
$$ax²+bx+c = a(x-{\color{teal}\frac{-b}{2a}})²$$

Si $\Delta > 0$ alors $x_1 = \frac{-b-\sqrt{\Delta}}{2a}$ et $x_2 = \frac{-b+\sqrt{\Delta}}{2a}$

$$ax²+bx+c = a(x-{\color{teal}x_1})(x-{\color{orange}x_2})$$
$$ax²+bx+c = a(x-{\color{teal}\frac{-b-\sqrt{\Delta}}{2a}})(x-{\color{orange}\frac{-b+\sqrt{\Delta}}{2a}})$$

Comme $\Delta = b² -4ac$ alors

$$ax²+bx+c = a(x-{\color{teal}\frac{-b-\sqrt{b² -4ac}}{2a}})(x-{\color{orange}\frac{-b+\sqrt{b² -4ac}}{2a}})$$

### Forme développée vers forme canonique

On a vu que $\alpha = \frac{-b}{2a}$ et $\beta = -\frac{\Delta}{4a} = -\frac{b²-4ac}{4a}$ donc

$$ax²+bx+c = a(x-{\color{teal}\alpha})²+{\color{orange}\beta}$$
$$a(x-{\color{teal}\frac{-b}{2a}})²+{\color{orange}-\frac{\Delta}{4a}}$$
$$a(x-{\color{teal}\frac{-b}{2a}})²-({\color{orange}\frac{b²-4ac}{4a}})$$


### Utilisation des identités remarquables

**Rappel des identités remarquables**  

$\color{teal}(a+b)² = a² + 2ab + b²$  
$\color{green}(a-b)² = a² - 2ab + b²$  
$\color{orange}(a+b)(a-b) = a² - b²$

On peut les utiliser dans certains cas pour passer d'une forme à l'autre.

Exemples :

$$\color{teal}f(x) = 4x²+16x+16$$
$$\color{teal}f(x) = 4(x²+4x+4)$$
$$\color{teal}f(x) = 4(x+2)²$$

$$\color{green}g(x) = 2x²-12x+18$$
$$\color{green}g(x) = 2(x²-6x+9)$$
$$\color{green}g(x) = 2(x-3)²$$

$$\color{orange}h(x) = 3x²-12$$
$$\color{orange}h(x) = 3(x²-4)$$
$$\color{orange}h(x) = 3(x-2)(x+2)$$

> [!NOTE]
> Pour identifier plus facilement les identités remarquables, quelques astuces :
> Si une identité remarquable est présente alors =>  
> b et c seront multiples de a (0 compte aussi pour b, on est alors dans le troisième cas).  
> b sera trèèèèèès probablement multiple de 2

On peut trouver la **forme canonique** avec une sorte "d'identité remarquable forcée".  
On rappelle qu'elle est de la forme $a(x-\alpha)²+\beta$. Si on ne s'occupe que de $a(x-\alpha)²$ alors on a une identité remarquable, celle de $\color{green}g(x)$ juste au dessus. $\beta$ est dans ce cas l'adaptation d'un $c$ qui ne convient pas pour faire une identité remarquable alors que $a$ et $b$ conviendraient.
On peut voir cela en reprenant $g(x)$ légèrement modifiée pour ne plus être une identité remarquable :

$$\color{green}g(x) = 2x²-12x+28$$

$$\color{green}g(x) = 2x²-12x+18+\color{red}10$$

On a enlevé 10 à $c$ et on l'a ajouté à la fin de l'équation pour retomber sur une identité remarquable.

$$\color{green}g(x) = 2(x-3)²+\color{red}10$$

$$\color{green}g(x) = a(x-\alpha)²+\color{red}\beta$$

On peut vérifier en calculant $\alpha$ et $\beta$ avec les formules vues plus haut.


$\alpha = \frac{-b}{2a}$

$\alpha = \frac{-(-12)}{2\times2} = 3$


$\beta = -\frac{\Delta}{4a}$

$\beta = -(\frac{b²-4ac}{4a})$

$\beta = -(\frac{(-12)²-4\times2\times28}{4\times2})$

$\beta = -(\frac{144-224}{8}) = 10$

## Produit et somme des racines

Pour deux nombres dont on connaît la somme S et le produit P, on peut trouver les deux nombres en résolvant l'équation suivante :

$x²-Sx+P=0$

Les deux nombres seront donc les racines $x_1$ et $x_2$ du pôlynome.

**Démonstration** :

On va pour cela utiliser la [forme factorisée](https://github.com/EtienneLancon/knowitall/blob/master/lycee/maths/001_polynomes_du_second_degre/cours.md#formes-dun-p%C3%B4lynome) de ce pôlynome

$$1(x-x_1)(x-x_2) = x² -xx_1-xx_2+x_1x_2$$

$$1(x-x_1)(x-x_2) = x² -(x_1+x_2)x+x_1x_2$$

$$1(x-x_1)(x-x_2) = x² -Sx+P$$