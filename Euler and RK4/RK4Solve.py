import numpy as np

#   Butcher Table:
#     0  | 
#    1/2 | 1/2
#    1/2 |  0  1/2
#     1  |  0   0   1
#    ____|________________
#        | 1/6 1/3 1/3 1/6

def RK4Solve(f,y0,T,h):
    # Initialize variables
    N = int(np.ceil((T[1]-T[0])/h))# number of steps
    h = (T[1]-T[0])/N # adjust step size to fit interval length
    d = len(y0) # dimension of solution
    t = np.linspace(T[0],T[1],N+1) # time grid
    y = np.zeros((d,N+1)) # solution
    y[:,0] = y0 # set initial value
    
    for j in range(0,N):
        y[:,j+1] = RK4Step(f,y[:,j],t[j],h)
         
    return np.array([t,y])



def RK4Step(f,y0,t0,h):

    k = np.zeros((len(y0),4))
      
    k[:,0] = f(t0,y0)
    k[:,1] = f(t0+h/2,y0+h/2*k[:,0])
    k[:,2] = f(t0+h/2,y0+h/2*k[:,1])
    k[:,3] = f(t0+h,y0+h*k[:,2])
    
    y1 = y0 + h/6 *(k[:,0]+2*k[:,1]+2*k[:,2]+k[:,3])
    
    return y1


