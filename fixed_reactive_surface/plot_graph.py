import numpy as np
from scipy import special
import matplotlib.pyplot as plt
import itertools

# Time series
T = [10, 50]

# Size
h = 0.015

# plot
plt.figure(figsize=(16, 9))
ax = plt.gca()

# marker tools
marker = itertools.cycle(('o', 'v', '^', '<', '>', 's', '8', 'p'))


for time in T:
    # read data from output
    data = np.loadtxt("dump_{}.last.xs".format(time), skiprows=9)

    # Get only at the boundary
    N = len(data[:,2])
    x, y = [], []
    for i in range(N):
        if (0.5 >= data[i,2]) and (0.1 <= data[i,2]):
            x.append(data[i, 2]/h)
            y.append(data[i, 5])

    # Revert the x
    x = x[::-1]

    color = next(ax._get_lines.prop_cycler)['color']
    plt.plot(x, y, linestyle='', markeredgecolor='none', marker=next(marker), color=color, label="sph-{}".format(time))
    
plt.ylabel("Concentration")
plt.xlim(np.min(x), np.max(x))
plt.ylim(np.min(y), np.max(y))
plt.xlabel("x")
plt.legend()
plt.savefig("results.png")

