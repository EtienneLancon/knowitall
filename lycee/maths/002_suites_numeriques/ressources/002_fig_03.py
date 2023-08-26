import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x = np.arange(0, 10) #intervalle [a;b[ du graphique

y = 100/2**x #courbe


abscisses = 0*x

plt.close()

###### abcisses
plt.plot(x, abscisses
            , color="orange"
            , markersize=0
            , label="abscisses")


###### courbe

plt.plot(x, y, marker="o"
            , color="blue"
            , markersize=8
            , label=r'$u_n = \frac{u_{n-1}}{2}$'
            , linestyle="None")


plt.legend(loc='best', fontsize=12)

plt.savefig(__file__[0:-3]+".png")