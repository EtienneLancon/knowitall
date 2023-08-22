import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x = np.arange(-3, 4)

y = -x**2 + 1

z = 0*x

plt.close()

cubic_interpolation_model = interp1d(x, y, kind = "cubic")

X_=np.linspace(x.min(), x.max(), 500)
Y_=cubic_interpolation_model(X_)
Z_=interp1d(x, z, kind = "cubic")(X_)

plt.plot(X_, Y_, markersize=8, label="-x² + 1")
plt.plot(X_, Z_, markersize=0, label="abscisses")

plt.legend(loc='best', fontsize=8)

plt.text(-1,0,r'$x_1$', fontsize=16, horizontalalignment='right', verticalalignment='bottom')
plt.text(1,0,r'$x_2$', fontsize=16, horizontalalignment='left', verticalalignment='bottom')

plt.savefig(__file__[0:-3]+".png")