import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x = np.arange(1, 15) #intervalle [a;b[ du graphique


y = 2/x + 0.5#courbe

abscisses = 0*x

limite = [0.5 for i in range(14)]

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
            , label="limite"
            , linestyle="dashed")


###### courbe

plt.plot(x, y, marker="o"
            , color="blue"
            , markersize=8
            , label=r'$\frac{2}{n} + \frac{1}{2}$'
            , linestyle="None")


plt.legend(loc='best', fontsize=12)


plt.text(13,0.4,r'$lim = \frac{1}{2}$', fontsize=16, horizontalalignment='center', verticalalignment='top')

plt.savefig(__file__[0:-3]+".png")