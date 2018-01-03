import numpy as np
from scipy import special
import matplotlib.pyplot as plt
import itertools

# Time series
T = [10]

# plot
plt.figure(figsize=(16, 9))
ax = plt.gca()

# marker tools
marker = itertools.cycle(('o', 'v', '^', '<', '>', 's', '8', 'p'))


for time in T:
    # read data from output
    data = np.loadtxt("dump_{}.last.xs".format(time), skiprows=9)

    color = next(ax._get_lines.prop_cycler)['color']
    plt.plot(data[:,2], data[:,5], linestyle='', markeredgecolor='none', marker=next(marker), color=color, label="sph-{}".format(time))
    
plt.ylabel("Concentration")
plt.xlim(np.min(data[:,2]), np.max(data[:,2]))
plt.ylim(np.min(data[:,5]), np.max(data[:,5]))
plt.xlabel("x")
plt.legend()
plt.savefig("results.png")

