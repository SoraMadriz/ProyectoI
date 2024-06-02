#Dependencias del modulo
import numpy as np #Manejo de matrices
import sympy as sp #Manejo de funciones
import psutil      #Estado de la computadora
#------------------------Entrada y salida del modulo----------------------------
# Entrada: recorrido                           -->  (dom)
#          número de divisiones del recorrido  -->  (n) 
#          condiciones iniciales               -->  (x_init,y_init,z_init) 
#          variables de las funciones          -->  (x,y,z,t)
#          funciones                           -->  (f1,f2,f3) 
#          pasos                               -->  (h)

# Salida: valores de la primera variable       -->  (x_values)
#         valores de la segunda variable       -->  (y_values)
#         valores de la tercera variables      -->  (z_values)
#         valores variable independiente       -->  (t_values)
#-------------------------------------------------------------------------------
def euler(dom,n,x_init,y_init,z_init,x,y,z,t,f1,f2,f3,h):
#vectores de salida
    t_values = []  #Particiones del dominio
    x_values = []  #Aproximaciones
    y_values = []  #Aproximaciones
    z_values = []  #Aproximaciones 

#Determinacion de pasos y diviciones
    if h is None:
        h=float((abs(dom[0]-dom[1]))/n)
    elif n is None:
        n=int((abs(dom[0]- dom[1]))/h)

#Declaración de condiciones iniciales
    t_begin = dom[0]   #Variable  de tiempo (independiente)
    x_begin = x_init   #Variable de corriente (dependiente)
    y_begin = y_init   #Variable de velocidad angular (dependiente)
    z_begin = z_init   #Variable de posición angular (dependiente)

#Valores Matriciales
    vector_bg = [x_begin,y_begin,z_begin]
    vector_fuction = sp.lambdify((x,y,z),[f1,f2,f3],modules="numpy")
    vector_bf = [0,0,0]
#Algoritmo de Euler
    for i in range(n+1):
    #Algoritmo de Euler
        vector_bf = np.array(vector_bg) + np.array(vector_fuction(*tuple(vector_bf)))*h
    #Se añaden los elementos x_begin y y_begin al array 
        t_values.append(t_begin)
        x_values.append(vector_bg[0])
        y_values.append(vector_bg[1])
        z_values.append(vector_bg[2])
    #verificacion y actualizacion en las variables:
        t_begin = t_begin + h
        vector_bg[0] = vector_bf[0]
        vector_bg[1] = vector_bf[1]
        vector_bg[2] = vector_bf[2]
    #Estado de la PC
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent

    return x_values, y_values,z_values, t_values,[cpu_usage,ram_usage]
