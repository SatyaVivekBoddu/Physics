import numpy as np

def ImpEulerSymplecticSolve(y0,T,h):

    # Initialize variables
    N = int(np.ceil((T[1]-T[0])/h))# number of steps
    h = (T[1]-T[0])/N # adjust step size to fit interval length
    d = len(y0) # dimension of solution
    t = np.linspace(0,12,N+1)				# time grid
    y = np.zeros((d,N+1)) # solution
    y[:,0] = y0 			# set initial value
    
    # Compute solution
    for j in range(0,N):
        y[0,j+1] = y[0,j]-h*(2-np.exp(y[1,j]))
        y[1,j+1] = y[1,j]+h*(1-np.exp(y[0,j+1]))
      
    return np.array([t,y])