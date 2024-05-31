import numpy as np
from scipy.integrate import odeint

# Definir las constantes del sistema
Ea = 350  # Voltaje
Ra = 10  # Inductancia
La = 100e-3  # Resistencia
kb = 7  # Constante de fricción
ki = 5  # Constante de inercia
Jm = 80  # Momento de inercia
bm = 20  # Coeficiente de fricción
Torque = 0  # Torque aplicado

# Definir las ecuaciones diferenciales
def sistema(y, t):
    i, w, theta = y
    di_dt = Ea/La - (Ra/La)*i - (kb/La)*w
    dw_dt = (ki/Jm)*i - (bm/Jm)*w - Torque/Jm
    dtheta_dt = w
    return [di_dt, dw_dt, dtheta_dt]

# Condiciones iniciales
y0 = [0, 0, 0]

# Definir los tiempos sobre los que se resolverá el problema
t = np.linspace(0, 3, 7)

# Resolver el sistema de ecuaciones diferenciales
sol = odeint(sistema, y0, t)

# Graficar las soluciones
print(sol[:,0])
print(sol[:,1])
print(sol[:,2])


import matplotlib.pyplot as plt
plt.figure()
plt.plot(t, sol[:, 0], label='i(t)')
plt.plot(t, sol[:, 1], label='w(t)')
plt.plot(t, sol[:, 2], label='theta(t)')
plt.xlabel('Tiempo')
plt.ylabel('Variables')
plt.legend()
plt.show()
