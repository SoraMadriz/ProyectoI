# Importación de modulos requeridos para trabajar
import numpy as np                #Trabajo con matrices
import matplotlib.pyplot as plt   #Gráficas
import pandas as pd               #Manejo de datos
from euler import euler           #Método de Euler
from graphics import graf         #Graficar salida de los métodos

#Declaración de las ecuaciones diferenciales
def f(i,w,theta):
    return (350/(100*10**(-3))) - (10/(100*10**(-3)))*i - (7/(100*10**(-3)))*w

def g(i,w,theta):
    return (5/80)*i - (20/80)*w

def h(i,w,theta):
    return w
#Función principal
def run():
#Declaración de funciones y variables a trabajar

#Métodos a utilizar
    f_euler, g_euler,h_euler,t_euler,i_euler=euler([0,3],None,0,0,0,f,g,h,0.5)
    
#Escritura de los valores por el método de Euler
    df_euler=pd.DataFrame({"ITERACIONES":i_euler,"x":f_euler,"y":g_euler,"z":h_euler})

    with pd.ExcelWriter('salida.xlsx') as writer:
        df_euler.to_excel(writer, sheet_name="Euler Method", index=False)

#Grafica
    graf(t_euler,h_euler,"Euler")

if __name__ == "__main__":
    run()
