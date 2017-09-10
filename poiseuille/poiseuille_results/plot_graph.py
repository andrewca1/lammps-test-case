import numpy as np
from scipy import special
import matplotlib.pyplot as plt
import itertools

# Parameters
F = 1.0e-4
nu = 1.0e-6
L = 1.0e-3
maxN = 100

# plot
plt.figure(figsize=(16, 9))
ax = plt.gca()

# marker tools
marker = itertools.cycle(('o', 'v', '^', '<', '>', 's', '8', 'p'))


# Poiseuille Flow
def f_pois(y, n, L, t):
    return 4*F*(L**2)/(nu*(np.pi**3)*((2*n+1)**3))*np.sin(np.pi*y*(2*n+1)/L)*np.exp(-(((2*n+1)*np.pi/L)**2)*nu*t)

# Collection of time step
T = [0.01, 0.045, 0.1125, 0.225, 0.8]
Tanalytical = [0.015, 0.06, 0.15, 0.25, 0.3]

# Try and plot
plt.figure(figsize=(20,9))

for i in range(5):
    # Analytical solution
    y = np.linspace(0.0, L, 1000)
    v_analytical = F/(2*nu)*(y-1e-6)*((y-1e-6) - L)
    for n in range(maxN):
        v_analytical = v_analytical + f_pois((y-1e-6),n,L,Tanalytical[i])

    # read data from output
    data = np.loadtxt("vel_{}.profile".format(T[i]), skiprows=4)

    color = next(ax._get_lines.prop_cycler)['color']
    plt.plot(data[:,1], -1.0*data[:,3], linestyle='', markeredgecolor='none', marker=next(marker), color=color, label="sph-{}".format(T[i]))
    plt.plot(y, v_analytical, label="analytical-{}".format(T[i]), linestyle='-', color=color)

plt.xlabel("y")
plt.ylabel("v_x")
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.savefig("poiseuille_results.png")
plt.legend(loc=3)
plt.savefig("results.png")
