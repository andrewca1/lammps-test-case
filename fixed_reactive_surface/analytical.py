import scipy.special as sp
import numpy as np
from scipy.optimize import brentq, fsolve
import matplotlib.pyplot as plt

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
    return J(0, alpha*r/r2)*(alpha*Y(1, alpha*r1/r2) + Da*Y(0, alpha*r1/r2)) \
        - Y(0, alpha*r/r2)*(alpha*J(1, alpha*r1/r2) + Da*J(0, alpha*r1/r2))

# Solve for alpha
f = lambda x : (x*Y(1, x*r1/r2) + Da*Y(0, x*r1/r2))*J(0, x) \
    - (x*J(1, x*r1/r2) + Da*J(0, x*r1/r2))*Y(0, x)

# Get analytical solution
def analytical(_X0, _t, _k, _Da, _C0, _Ceq, _r1, _r2, _nval):
    _A = fsolve(f, _X0)
    # Filtered out some duplicate elements
    _A = list(set(_A))
    # Sort
    _A.sort()
    
    # Remove one more elements
    _tol = 1.0e-6
    _delA = []
    _temp = _A[0]
    for _i in range(len(_A)):
        if (abs(_A[_i]-_A[_i-1]) <= _tol):
            _delA.append(_A[_i])
            
    # Get the final roots
    _alphas = [_x for _x in _A if _x not in _delA]
    
    # Now we can obtain the concentration
    _xr = np.linspace(_r1, _r2, _nval)

    # Summing the transient term
    _C = _xr*0.0
    for _alpha in _alphas:
        _C -= np.pi*np.exp(-(_alpha**2)*_t*_k/(_r2*_Da))*(_Da**2)*(J(0, _alpha)**2)*B(_xr, _alpha)*(1 - _Ceq/_C0)/F(_alpha)

    # Adding the solution
    _C += 1.0 + (_r1/_r2)*_Da*(1 - _Ceq/_C0)*np.log(_xr/_r2)/(1 + (_r1/_r2)*_Da*np.log(_r2/_r1))
    _C = _C*_C0

    return _xr, _C, _alphas

# Parameters
h = 1.0
r1, r2 = 3.0*h, 15.0*h
Ceq, C0 = 0.0, 1.0
D = 1.0
R = 8.0e-3

# Get a number of results
X0 = np.arange(1.0, 60.0, 4.0)

# Plot the analytical solution
# TODO: Why the constant factor?
k = R*0.89
Da = k*r2/D 
xr, C, alphas = analytical(X0, 50, k, Da, C0, Ceq, r1, r2, 10000)
plt.plot(xr/h, C, label="t=50")

# Size
h = 0.03125
r1 = 3.0*h
times = [50]
for time in times:
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

    plt.scatter(x, y, s=10, label="sph-{}".format(time))
    
plt.legend(loc=4)
plt.show()
