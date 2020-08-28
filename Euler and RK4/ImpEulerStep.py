from numpy import linalg as LA

def ImpEulerStep(f,y0,t0,h,tol):

    # Initialize
    t1 = t0+h
    
    # Initial estimate
    f0 = y0
    Y1 = y0 + h*f(t1,y0)
    
    errNorm = LA.norm(Y1-f0)
    
    # Fixed point iteration
    i = 0;
    while errNorm > h*tol:
        Y1old = Y1
        Y1 = y0 + h*f(t1,Y1old)
        errNorm = LA.norm(Y1-Y1old)
        i = i+1
        if(i>=1e5):
            print('Fixed point iteration terminated after %d steps with error %g\n',i,errNorm)
            break
    
    # Define solution at next timestep
    y1 = Y1
    
    return y1
