import numpy as np

#Entrada: recorrido(dom),número de divisiones del recorrido(n), 
#         condiciones iniciales(x_init,y_init), funcion(f), pasos(h)

#SALIDA: Aproximación(y_values)

def euler(dom,n,x_init,y_init,z_init,f1,f2,f3,h):
    #Lista de salida
    t_values = []   #Particiones del dominio
    x_values = []  #Aproximaciones
    y_values = []  #Aproximaciones
    z_values = []  #Aproximaciones 
    iteration = [] #Iteraciones

    #Definición del paso:
    if h is None:
        h=(abs(dom[0]-dom[1]))/n
        print(h)
    elif n is None:
        n=int((abs(dom[0]- dom[1]))/h)

    #Declaración de condiciones iniciales
    t_begin = dom[0]
    x_begin = x_init
    y_begin = y_init
    z_begin = z_init
    i=0

    #Algoritmo de Euler
    for i in range(n+1):
        x_bef = x_begin + f1(x_begin,y_begin,z_begin)*h
        y_bef = y_begin + f2(x_begin,y_begin,z_begin)*h
        z_bef = z_begin + f3(x_begin,y_begin,z_begin)*h
    #Se añaden los elementos x_begin y y_begin al array 
        t_values.append(t_begin)
        x_values.append(x_begin)
        y_values.append(y_begin)
        z_values.append(z_begin)
        iteration.append(i)
    #verificacion y actualizacion en las variables:
        t_begin = t_begin + h
        x_begin = x_bef
        y_begin = y_bef
        z_begin = z_bef
    return x_values, y_values,z_values, t_values, iteration
