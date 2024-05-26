import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from euler import euler
from graphics import graf

#Declaración de las ecuaciones diferenciales
def f(i,w,theta):
    return (350/(100*10**(-3))) - (10/(100*10**(-3)))*i - (7/(100*10**(-3)))*w

def g(i,w,theta):
    return (5/80)*i - (20/80)*w

def h(i,w,theta):
    return theta
#Función principal
def run():
    f_euler, g_euler,h_euler,t_euler,i_euler=euler([0,3],None,0,0,0,f,g,h,0.5)
    
#Escritura de los valores por el método de Euler
    df_euler=pd.DataFrame({"ITERACIONES":i_euler,"x":f_euler,"y":g_euler,"z":h_euler})

#Escritura en el Excel
    with pd.ExcelWriter('salida.xlsx') as writer:
        df_euler.to_excel(writer, sheet_name="Euler Method", index=False)

#Grafica
    graf(t_euler,f_euler,"Euler")

if __name__ == "__main__":
    run()
