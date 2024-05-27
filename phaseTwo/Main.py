# Importación de modulos requeridos para trabajar
import numpy as np                #Trabajo con matrices
import matplotlib.pyplot as plt   #Gráficas
import pandas as pd               #Manejo de datos
import sympy as sp                #Matemática simbólica
from Euler import euler           #Método de Euler
from graphics import graf         #Graficar salida de los métodos

def run():
#Declaración de funciones y variables a trabajar
    i,w,theta,t = sp.symbols('i w theta t');
    #Corriente de armadura di(t)/dt
    f = sp.sympify((350/(100*10**(-3))) - (10/(100*10**(-3)))*i - (7/(100*10**(-3)))*w)
    #aceleracion angular del motor dw/dt
    g = sp.sympify((5/80)*i - (20/80)*w)
    #Velocidad angular del motor dtheta/dt
    h = sp.sympify(w)


#Métodos a utilizar
    f_euler, g_euler,h_euler,t_euler,i_euler=euler([0,3],None,0,0,0,i,w,theta,t,f,g,h,1.5)
    
#Escritura en el archivo .xlsx
    #Declaración de los DataFrame
    df_euler=pd.DataFrame({"ITERACIONES":i_euler,"x":f_euler,"y":g_euler,"z":h_euler})
    #Escritura
    with pd.ExcelWriter('Salida.xlsx') as writer:
        df_euler.to_excel(writer, sheet_name="Euler Method", index=False)

#Modulos para graficar
    path = "/home/leonardomadriz/Universidad/Apuntes/TercerAño/CT3233-PotenciaI/Proyecto/Codigo/phaseTwo/grafica/Salida_Euler"
    graf(t_euler,f_euler,"Euler",path,"Corriente vs Tiempo")
    graf(t_euler,g_euler,"Euler",path,"Velocidad angular vs Tiempo")
    graf(t_euler,h_euler,"Euler",path,"Posición angular vs Tiempo")

if __name__ == "__main__":
    run()
