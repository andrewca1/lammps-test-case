import numpy as np
from scipy import special
import matplotlib.pyplot as plt
import itertools

import os

path, dirs, files = os.walk("./results").__next__()
file_count = len(files)

# plot
plt.figure(figsize=(16, 9))
ax = plt.gca()

# # marker tools
# marker = itertools.cycle(('o', 'v', '^', '<', '>', 's', '8', 'p'))

# Initial list
cA = []; cB = []; cC = []

for i in range(file_count):
    # # analytical solution
    # x = np.linspace(0.0, 1.0, 100)
    
    # read data from output
    data = np.loadtxt(path+"/dump{}.dat".format(i), skiprows=9)
    cAt, cBt, cCt = data[:,5], data[:,6], data[:,7]

    cA.append(np.mean(cAt))
    cB.append(np.mean(cBt))
    cC.append(np.mean(cCt))
    
    # color = next(ax._get_lines.prop_cycler)['color']
    # plt.plot(data[:,2], data[:,5], linestyle='', markeredgecolor='none', marker=next(marker), color=color, label="sph-{}".format(time))

cA, cB, cC = np.array(cA), np.array(cB), np.array(cC)
    
t = 0.025*np.arange(0,len(cA))
k = 50.0e-4

if (cA[0] == cB[0]):
    plt.plot(t, 1.0/np.array(cA), '*', label='sph')
    plt.plot(t, k*t+(1.0/cA[0]), '-', label='analytical')
else:
    plt.plot(t, k*t*(cB[0] - cA[0]), '-', label='analytical')
    plt.plot(t, np.log((cB*cA[0])/(cA*cB[0])), '*', label='sph')
             
plt.ylabel("Concentration")
plt.xlabel("t")
plt.legend()
plt.savefig("graph.png")

