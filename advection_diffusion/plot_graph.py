import numpy as np
from scipy import special
import matplotlib.pyplot as plt

# parameters
alpha = 1.0e-4
time  = 4.0
vel   = 1.0
el    = 2.0
er    = 1.0

# domain
Lx = 1.0
# splitting point
xc = 0.5*Lx + vel*time*0.01

# analytical solution
x = np.linspace(0.0, 1.0, 100)
e_analytic = 0.5*(er + el) + 0.5*(er - el)*special.erf((x-xc)/np.sqrt(4*alpha*time))

# read data from output
data = np.loadtxt("dump.last", skiprows=9)

# plot
fig = plt.figure()
plt.plot(x, e_analytic, label="analytical")
plt.scatter(data[25:180,2], data[25:180,5], color="green", label="sph")
plt.ylabel("Temperature")
plt.ylim(0.8, 2.2)
plt.xlim(0.0, 1.0)
plt.xlabel("x")
plt.legend()
plt.savefig("results.png")

