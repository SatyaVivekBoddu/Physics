import numpy as np
import matplotlib.pyplot as plt

from EulerSolve import EulerSolve
from ImpEulerSolve import ImpEulerSolve
from ImpMidPointSolve import ImpMidPointSolve
from ImpMidPointSolveWithEuler import ImpMidPointSolveWithEuler
from RK4Solve import RK4Solve

# Defines right hand side
def f(t,y):
    return np.array([y[1],-np.sin(y[0])])

# Defines problem and discretization parameters
y0 = [np.pi/2,0]
T = [0,8]
h = 0.25
tol = 0.0001

# Computes solutions
[t,yExp] = EulerSolve(f, y0, T, h)
[t,yImp] = ImpEulerSolve(f, y0, T, h, tol)
[t,yImpMidPoint] = ImpMidPointSolve(f, y0, T, h, tol) #Replacable with ImpMidpoint using explicit halfstep
[t,yRK4] = RK4Solve(f, y0, T, h)

# Plots solution as a function of time
plt.figure()
plt.plot(t[:],yExp[0,:],'cadetblue',label="Euler Explicit")
plt.plot(t[:],yImp[0,:],'tomato',label="Euler Implicit")
plt.plot(t[:],yRK4[0,:],'slategray',marker='o',markersize=3,label="RK4")
plt.plot(t[:],yImpMidPoint[0,:],'orchid',label="Euler Implicit MidPoint")

plt.title('Numerical methods for the mathematical pendulum in time')
plt.legend(loc="upper left")
plt.xlabel('t') 
plt.ylabel('x') 

# Plots solution in phase space and against time
plt.figure()
plt.plot(np.mod(yExp[0,:]+np.pi,2*np.pi)-np.pi, yExp[1,:],'cadetblue',label="Euler Explicit")
plt.plot(np.mod(yImp[0,:]+np.pi,2*np.pi)-np.pi, yImp[1,:],'tomato',label="Euler Implicit")
plt.plot(np.mod(yRK4[0,:]+np.pi,2*np.pi)-np.pi, yRK4[1,:],'slategray',marker='o',markersize=3,label="RK4")
plt.plot(np.mod(yImpMidPoint[0,:]+np.pi,2*np.pi)-np.pi, yImpMidPoint[1,:],'orchid',label="Euler Implicit MidPoint")


plt.title('Numerical methods for the mathematical pendulum in phase space')
plt.legend(loc="upper left")
plt.xlabel('x') 
plt.ylabel('dx/dt') 


############################################################################
############################################################################
# At large times
T = [0,500]
h = 1

# Computes solutions
[t,yImpMidPoint] = ImpMidPointSolve(f, y0, T, h, tol)
[t,yRK4] = RK4Solve(f, y0, T, h)

# Plots solution in phase space and against time in new figure
plt.figure()
plt.plot(np.mod(yImpMidPoint[0,:]+np.pi,2*np.pi)- np.pi,yImpMidPoint[1,:],'orchid',label="Euler Implicit Midpoint")
plt.plot(np.mod(yRK4[0,:]+np.pi,2*np.pi)- np.pi,yRK4[1,:],'slategray',label="RK4")
plt.legend(loc="upper left")
plt.xlabel('x') 
plt.ylabel('dx/dt') 
plt.title('Numerical methods for the mathematical pendulum in time in phase space')

plt.figure()
plt.plot(t[0:200],yImpMidPoint[0,0:200],'orchid',label="Euler Implicit MidPoint")
plt.plot(t[0:200],yRK4[0,0:200],'slategray',label="RK4")
plt.legend(loc="upper left")
plt.xlabel('t') 
plt.ylabel('x')
plt.title('Numerical methods for the mathematical pendulum in time at long times')


############################################################################
############################################################################
# Hamiltonian

# Create invariant vectors
invaExp=np.zeros(len(yExp[0]))
invaImp=np.zeros(len(yExp[0]))
invaImpMidPoint=np.zeros(len(yExp[0]))
invaRK4=np.zeros(len(yExp[0]))


# Compute invariant
for j in range(len(yExp[0])):
    invaExp[j]=yExp[1,j]**2/2-np.cos(yExp[0,j])
    invaImp[j]=yImp[1,j]**2/2-np.cos(yImp[0,j])
    invaImpMidPoint[j]=yImpMidPoint[1,j]**2/2- np.cos(yImpMidPoint[0,j])
    invaRK4[j]=yRK4[1,j]**2/2-np.cos(yRK4[0,j])
    
    
# Plots Hamiltonian as a function of time    
plt.figure()
plt.plot(invaExp,'cadetblue',label="Euler Explicit")
plt.plot(invaImp,'tomato',label="Euler Implicit")
plt.plot(invaImpMidPoint,'orchid',label="Euler Implicit MidPoint")
plt.plot(invaRK4,'slategray',label="RK4")
plt.legend(loc="upper left")
plt.xlabel('t') 
plt.ylabel('H(p,q)')
plt.title('Hamiltonian over time')

