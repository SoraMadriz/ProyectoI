import numpy as np
from scipy.integrate import odeint

def isopy(Ra, Ea, La, kb, ki, Jm, bm, Tl):
    def sistema(y, t):
        i, w, theta = y
        di_dt = Ea/La - (Ra/La)*i - (kb/La)*w
        dw_dt = (ki/Jm)*i - (bm/Jm)*w - Tl/Jm
        dtheta_dt = w
        return [di_dt, dw_dt, dtheta_dt]

# Condiciones iniciales
    y0 = [0, 0, 0]

# Definir los tiempos sobre los que se resolverá el problema
    t = np.linspace(0, 3, 7)

# Resolver el sistema de ecuaciones diferenciales
    sol = odeint(sistema, y0, t)

    return sol, t
