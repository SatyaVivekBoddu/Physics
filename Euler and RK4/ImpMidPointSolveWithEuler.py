import numpy as np
from EulerStep import EulerStep
from ImpEulerStep import ImpEulerStep

def ImpMidPointSolveWithEuler(f,y0,T,h,tol):

    # Initialize variables
    N = int(np.ceil((T[1]-T[0])/h))# number of steps
    h = (T[1]-T[0])/N # adjust step size to fit interval length
    d = len(y0) # dimension of solution
    t = np.linspace(T[0],T[1],N+1) # time grid
    y = np.zeros((d,N+1)) # solution
    y[:,0] = y0 # set initial value
    
    # Compute solution
    for j in range(0,N):
        yhalf = ImpEulerStep(f, y[:,j], t[j], h/2, tol)
        y[:,j+1] = EulerStep(f, yhalf, t[j], h/2)

    return np.array([t,y])
