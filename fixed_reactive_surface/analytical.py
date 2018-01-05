import scipy.special as sp
import numpy as np
from scipy.optimize import brentq, fsolve
import matplotlib.pyplot as plt

# Parameters
r1, r2 = 3, 15
Ceq, C0 = 0.0, 1.0
D = 1
d = 0.5
k = 1.14
Da = k*r2/D
t = 0.0

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
X0 = np.linspace(0.1, 1.0, 100)
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
alphas = [alphas[0]]

# Now we can obtain the concentration
xr = np.linspace(r1, r2, 10000)
C = xr*0.0
for alpha in alphas:
    C += np.pi*np.exp(-(alpha**2)*t*k/(r2*Da))*(Da**2)*(J(0, alpha)**2)*B(xr, alpha)*(1 - Ceq/C0)/F(alpha)

C = 1.0 + (r1/r2)*Da*(1 - Ceq/C0)*np.log(xr/r2)/(1 + (r1/r2)*Da*np.log(r2/r1)) - C

# Plot the solution
plt.plot(xr, C)
plt.show()
