import scipy.special as sp
import numpy as np
from scipy.optimize import brentq, fsolve
import matplotlib.pyplot as plt

# Parameters
r1, r2 = 7, 30
Ceq, C0 = 0.0, 1.0
D = 1
d = 0.5
k = 1.14
Da = k*r2/D

# Bessel function of the first kind
def J(n, x):
    return sp.jn(n, x)

# Bessel function of the second kind
def Y(n, x):
    return sp.yn(n, x)

# Define function F
def F(alpha):
    return (alpha*J(1, alpha*r1/r2) + Da*J(0, alpha*r1/r2))**2 \
        - (alpha**2 + Da**2)*(J(0, alpha))**2

# Define function B
def B(r, alpha):
    return J(0, alpha*r/r2)*(alpha*Y(1, alpha*r1/r2)) + Da*Y(0, alpha*r1/r2) \
        - Y(0, alpha*r/r2)*(alpha*J(1, alpha*r1/r2) + Da*J(0, alpha*r1/r2))

# Solve for alpha
f = lambda x : (x*Y(1, x*r1/r2) + Da*Y(0, x*r1/r2))*J(0, x) \
    - (x*J(1, x*r1/r2) + Da*J(0, x*r1/r2))*Y(0, x)

# Get a number of results
X0 = np.arange(3.0, 60.0, 4.0)
A = fsolve(f, X0)
# Filtered out some duplicate elements
A = list(set(A))
# Sort
A.sort()

# Remove one more elements
tol = 1.0e-6
delA = []
temp = A[0]
for i in range(len(A)):
    if (abs(A[i]-A[i-1]) <= tol):
        delA.append(A[i])

# Get the final roots
alphas = [x for x in A if x not in delA]

# Now we can obtain the concentration
xr = np.linspace(r1, r2, 10000)
times = [235, 270]

for t in times:
    C = xr*0.0
    for alpha in alphas:
        C += np.pi*np.exp(-(alpha**2)*t*k/(r2*Da))*(Da**2)*(J(0, alpha)**2)*B(xr, alpha)*(1 - Ceq/C0)/F(alpha)

    C = 1.0 + (r1/r2)*Da*(1 - Ceq/C0)*np.log(xr/r2)/(1 + (r1/r2)*Da*np.log(r2/r1)) - C
    
    # Plot the solution
    plt.plot(xr, C, label="t={}".format(t))

h = 0.015
times = [10, 50]
    
for time in times:
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
    plt.scatter(x, y, linestyle='-', s=5, label="sph-{}".format(time))
    
plt.legend(loc=4)
plt.show()
