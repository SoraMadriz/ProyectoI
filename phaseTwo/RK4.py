#Dependencias del modulo
import sympy as sp #Manejo de funciones
import psutil      #Estado de la computadora
import numpy as np # Matrices
#------------------------Entrada y salida del modulo----------------------------
# Entrada: recorrido                           -->  (dom)
#          número de divisiones del recorrido  -->  (n) 
#          condiciones iniciales               -->  (x_init,y_init,z_init) 
#          variables de las funciones          -->  (x,y,z,t)
#          funciones                           -->  (f1,f2,f3) 
#          pasos                               -->  (h)

# Salida: valores de la primera variable       -->  (x_values)
#         valores variable independiente       -->  (y_values)
#-------------------------------------------------------------------------------
def rungeKutta(dom,n,x_init,y_init,z_init,x,y,z,t,f1,f2,f3,h):
#vectores de salida
    y_values = []  #Soluciones, fila1=x, fila2=y, fila3=z
    t_values = []  #Valores del tiempo

#Determinacion de pasos y diviciones
    if h is None:
        h=(abs(dom[0]-dom[1]))/n
    elif n is None:
        n=int((abs(dom[0]- dom[1]))/h)

#Arreglo en los datos del problema
    y_bg = [x_init,y_init,z_init]                               #Vector valores iniciales
    t = dom[0]                                                  #Valor inicial del tiempo
    function = sp.lambdify((x,y,z),[f1,f2,f3],modules='numpy')  #vector de funciones
    y_values.append(y_bg)                                       #Valor inicial
    t_values.append(t)                                          #Valor inicial
#Método de RK4
    for i in range(1,n+1):
        k1 = np.array(function(*(y_values[i-1][0],y_values[i-1][1],y_values[i-1][2])))
        k2 = np.array(function(*(y_values[i-1][0]+k1[0]*(h/2),y_values[i-1][1]+k1[1]*(h/2),y_values[i-1][2]+k1[2]*(h/2))))
        k3 = np.array(function(*(y_values[i-1][0]+k2[0]*(h/2),y_values[i-1][1]+k2[1]*(h/2),y_values[i-1][2]+k2[2]*(h/2))))
        k4 = np.array(function(*(y_values[i-1][0]+k3[0]*h,y_values[i-1][1]+k3[1]*h,y_values[i-1][2]+k3[2]*h,)))
        y1_sol = y_values[i-1][0]+(k1[0]+2*k2[0]+2*k3[0]+k4[0])*(h/6)                      
        y2_sol = y_values[i-1][1]+(k1[1]+2*k2[1]+2*k3[1]+k4[1])*(h/6)
        y3_sol = y_values[i-1][2]+(k1[2]+2*k2[2]+2*k3[2]+k4[2])*(h/6)
        y_values.append([y1_sol,y2_sol,y3_sol])
        t=t+h
        t_values.append(t)
    #Estado de la computadora
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    return y_values,t_values, [cpu_usage,ram_usage]

