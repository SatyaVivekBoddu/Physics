import numpy as np
import matplotlib.pyplot as plt

from EulerSolve import EulerSolve
from ImpEulerSolve import ImpEulerSolve
from ImpEulerSymplecticSolve import ImpEulerSymplecticSolve

# Define problem and discretization parameters
y0 = [2,2]
T = [0,12]
h = 0.05
tol = 1e-6

# Define right hand side  p -> y(1) and q-> y(2) 
def f(t,y):
    return np.array([np.exp(y[1])-2,1-np.exp(y[0])])

# Explicit Euler (2) and Implicit Euler method (3)
[t,yExp] = EulerSolve(f,y0,T,h);
[t,yImp] = ImpEulerSolve(f,y0,T,h,tol);

# Implicit Euler method for the given symplectic system in (4)
[t,yImpSymp] = ImpEulerSymplecticSolve(y0,T,h);

# Compute the graph of invariance
Inva_exp = yExp[0,:]-np.exp(yExp[0,:])+2*yExp[1,:]-np.exp(yExp[1,:])
Inva_imp = yImp[0,:]-np.exp(yImp[0,:])+2*yImp[1,:]-np.exp(yImp[1,:])
Inva_impsym = yImpSymp[0,:]-np.exp(yImpSymp[0,:])+2*yImpSymp[1,:]-np.exp(yImpSymp[1,:])

# Plot graph of invariance
plt.figure()
plt.plot(t,Inva_exp,label="Euler Explicit")
plt.plot(t,Inva_imp,label="Euler Implicit")
plt.plot(t,Inva_impsym,label="Symplectic Euler")
plt.legend(loc="lower left")

plt.xlim([min(t),max(t)])
plt.title('Trajectory of Invariance I(p,q) under different algorithms');
plt.xlabel('t')
plt.ylabel('I')

# Plot solutions in phase space
plt.figure()
plt.plot(yExp[0,:], yExp[1,:],'bo-',label="Euler Explicit")
plt.plot(yImp[0,:], yImp[1,:],'r^-',label="Euler Implicit")
plt.plot(yImpSymp[0,:], yImpSymp[1,:],'gx-',label="Symplectic Euler")

plt.title('Numerical Methods for a Hamiltonian system')
plt.legend(loc="lower left")
plt.xlabel('p') 
plt.ylabel('q') 