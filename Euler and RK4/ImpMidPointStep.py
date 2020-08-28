from numpy import linalg as LA

def ImpMidPointStep(f,y0,t0,h,tol):

    # Initial estimate
    f0 = y0
    Y1 = y0 + h*f(t0+h/2,y0)
    errNorm = LA.norm(Y1-f0)
    
    # Fixed point iteration
    i = 0
    while errNorm > tol:
        Y1old = Y1
        Y1 = y0 + h*f(t0+h/2,1/2*(y0+Y1old)) # y0 constant
        errNorm = LA.norm(Y1-Y1old)
        i = i + 1
        if(i>=1e5):
            print('Fixed point iteration terminated after %d steps with error %g\n',i,errNorm)
            break

    # Define solution and feval at next timestep
    y1 = Y1
    
    return y1
