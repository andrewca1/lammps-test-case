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
def F(_alpha, _r1, _r2, _Da):
    return (_alpha*J(1, _alpha*_r1/_r2) + _Da*J(0, _alpha*_r1/_r2))**2 \
        - (_alpha**2 + _Da**2)*(J(0, _alpha))**2

# Define function B
def B(_r, _alpha, _r1, _r2, _Da):
    return J(0, _alpha*_r/_r2)*(_alpha*Y(1, _alpha*_r1/_r2) + _Da*Y(0, _alpha*_r1/_r2)) \
        - Y(0, _alpha*_r/_r2)*(_alpha*J(1, _alpha*_r1/_r2) + _Da*J(0, _alpha*_r1/_r2))

# Solve for alpha
def f(x, *data):
    _r1, _r2, _Da = data
    return (x*Y(1, x*_r1/_r2) + _Da*Y(0, x*_r1/_r2))*J(0, x) \
        - (x*J(1, x*_r1/_r2) + _Da*J(0, x*_r1/_r2))*Y(0, x)

# Get analytical solution
def analytical(_X0, _t, _k, _Da, _C0, _Ceq, _r1, _r2, _nval):
    data = (_r1, _r2, _Da)
    _A = fsolve(f, _X0, args=data)
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
        _C -= np.pi*np.exp(-(_alpha**2)*_t*_k/(_r2*_Da))*(_Da**2)*(J(0, _alpha)**2)* \
              B(_xr, _alpha, _r1, _r2, _Da)*(1 - _Ceq/_C0)/F(_alpha, _r1, _r2, _Da)

    # Adding the solution
    _C += 1.0 + (_r1/_r2)*_Da*(1 - _Ceq/_C0)*np.log(_xr/_r2)/(1 + (_r1/_r2)*_Da*np.log(_r2/_r1))
    _C = _C*_C0

    return _xr, _C, _alphas

# Parameters
h = 0.03125
r1, r2 = 3.0*h, 15.0*h
Ceq, C0 = 0.0, 1.0
D = 1.0
R = 8.0e-2

times = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5]

# Get a number of results
X0 = np.arange(1.0, 60.0, 4.0)

# Plot the analytical solution
# TODO: Why the constant factor?
k = [R*0.15, R*0.15, R*0.15, R*0.15, R*0.15, R*0.15]

for i in range(len(times)):
    Da = k[i]*r2/D
    xr, C, alphas = analytical(X0, times[i], k[i], Da,
                               C0, Ceq, r1, r2, 10000)
    plt.plot(xr/h, C, label="t={}".format(times[i]))

# # SPH
# for time in times:
#     # read data from output
#     data = np.loadtxt("dump_{}.last.xs".format(time), skiprows=9)
#     dx = data[0,2]
    
#     # Get only at the boundary
#     N = len(data[:,2])
#     x, y = [], []
#     for i in range(N):
#         if (data[i,2] >= (0.5+r1)) and (abs(data[i,3]-0.5) <= (dx)):
#             x.append((data[i, 2]-0.5)/h)
#             y.append(data[i, 5])

#     plt.scatter(x, y, s=10, label="sph-{}".format(time))
    
plt.legend(loc=4)
plt.show()
