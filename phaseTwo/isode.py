from scipy.integrate import odeint
import numpy as np
import sympy as sp
def isopy(f1,f2,f3,x,y,z,t):
#Ecuaciones differenciales
    eq1 = sp.Eq(sp.diff(x,t),f1)
    eq2 = sp.Eq(sp.diff(y,t),f2)
    eq1 = sp.Eq(sp.diff(z,t),f3)
    def system(t,u):
        x,y,z = u
        da = f1
        db = f2
        dc = f3
    return dx, dydt, dzdt
    solution = solver_ivp(system, [0,0,0], [0,0,0], t_eval=np.linspace(0,10,100))

