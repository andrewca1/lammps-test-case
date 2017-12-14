import numpy as np
from scipy import special
import matplotlib.pyplot as plt
import itertools

# parameters
alpha = 1.0e-3
K = 0.0
el    = 2.0
er    = 1.0

# domain
Lx = 1.0
# splitting point
xc = 0.5*Lx

# Time series
T = [10]

# plot
plt.figure(figsize=(16, 9))
ax = plt.gca()

# marker tools
marker = itertools.cycle(('o', 'v', '^', '<', '>', 's', '8', 'p'))


for time in T:
    # analytical solution
    x = np.linspace(0.0, 1.0, 100)
    e_analytic = 0.5*(el+er) + 0.5*(er - el)*special.erf((x-xc)/np.sqrt(4*alpha*time))
    e_analytic = np.exp(-K*time)*e_analytic
    
    # read data from output
    data = np.loadtxt("dump_{}.last".format(time), skiprows=9)

    color = next(ax._get_lines.prop_cycler)['color']
    plt.plot(data[:,2], data[:,5], linestyle='', markeredgecolor='none', marker=next(marker), color=color, label="sph-{}".format(time))
    plt.plot(x, e_analytic, label="analytical-{}".format(time), linestyle='-', color=color)
    
plt.ylabel("Temperature")
plt.ylim(0.8, 2.2)
plt.xlim(0.0, Lx)
plt.xlabel("x")
plt.legend()
plt.savefig("results.png")

