import numpy as np
from scipy import special
import matplotlib.pyplot as plt
import itertools

# Parameters
V = 6.0e-5
nu = 1.0e-6
L = 1.0e-3
maxN = 100

# plot
plt.figure(figsize=(16, 9))
ax = plt.gca()

# marker tools
marker = itertools.cycle(('o', 'v', '^', '<', '>', 's', '8', 'p'))


# Couette flow
def f_coue(y, n, L, t):
    return (2*V/(n*np.pi))*((-1)**n)*np.sin(n*np.pi*(y/L))*np.exp(-1.0*nu*t*((n*(np.pi/L))**2))

# Collection of time step
T = [0.01, 0.045, 0.1125, 0.225, 0.8]
Tanalytical = [0.015, 0.065, 0.15, 0.25, 0.3]

# Try and plot
plt.figure(figsize=(20,9))

for i in range(4):
    # Analytical solution
    y = np.linspace(0.0, L, 1000)
    v_analytical = (V/L)*y
    for n in range(1,maxN):
        v_analytical = v_analytical + f_coue((y-1e-6),n,L,Tanalytical[i])

    # read data from output
    data = np.loadtxt("vel_{}.profile".format(T[i]), skiprows=4)

    color = next(ax._get_lines.prop_cycler)['color']
    plt.plot(data[2:-2,1], data[2:-2,3], linestyle='', markeredgecolor='none', marker=next(marker), color=color, label="sph-{}".format(T[i]))
    plt.plot(y+0.05e-6, v_analytical+0.05e-5, label="analytical-{}".format(T[i]), linestyle='-', color=color)

plt.xlabel("y")
plt.ylabel("v_x")
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.legend(loc=2)
plt.savefig("results.png")
