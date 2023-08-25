import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x = np.arange(1, 21) #intervalle [a;b[ du graphique


y = x/4#courbe

abscisses = 0*x

limite = [5 for i in range(20)]

plt.close()

###### abcisses
plt.plot(x, abscisses
            , color="orange"
            , markersize=0
            , label="abscisses")

###### limite

plt.plot(x, limite
            , color="red"
            , markersize=0
            , label=r'$u_n + u_0$'
            , linestyle="dashed")


###### courbe

plt.plot(x, y, marker="o"
            , color="blue"
            , markersize=8
            , label=r'$u_n = u_{n-1}+\frac{1}{4}$'
            , linestyle="None")


plt.legend(loc='best', fontsize=12)

plt.savefig(__file__[0:-3]+".png")