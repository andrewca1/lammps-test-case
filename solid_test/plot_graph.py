import numpy as np
from scipy import special
import matplotlib.pyplot as plt
import itertools

# Time series
T = [0.005]

# Size
h = 0.03125
r1 = 3.0*h

# plot
plt.figure(figsize=(16, 9))
ax = plt.gca()

# marker tools
marker = itertools.cycle(('o', 'v', '^', '<', '>', 's', '8', 'p'))


for time in T:
    # read data from output
    data = np.loadtxt("dump_{}.last.xs".format(time), skiprows=9)
    dx = data[0,2]
    
    # Get only at the boundary
    N = len(data[:,2])
    x, y = [], []
    for i in range(N):
        if (data[i,2] >= (0.5+r1)) and (abs(data[i,3]-0.5) <= (dx)):
            x.append((data[i, 2]-0.5)/h)
            y.append(data[i, 5])

    color = next(ax._get_lines.prop_cycler)['color']
    plt.plot(x, y, linestyle='', markeredgecolor='none', marker=next(marker), color=color, label="sph-{}".format(time))
    
plt.ylabel("Concentration")
plt.xlabel("x")
plt.legend()
plt.show()
# plt.savefig("results.png")

