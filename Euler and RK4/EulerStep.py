def EulerStep(f,y0,t0,h):
    return y0 + h*f(t0,y0)
