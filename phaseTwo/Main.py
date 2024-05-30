# Importación de modulos requeridos para trabajar
import numpy as np                #Trabajo con matrices
import matplotlib.pyplot as plt   #Graficas
import pandas as pd               #Manejo de datos
import sympy as sp                #Matemática simbólica
from Euler import euler           #Metodo de Euler
from Heun import heun             #Metodo de Heun
from RK4 import rungeKutta        #Metodo de RK4
from graphics import graf         #Graficar salida de los métodos

def run():
#Declaracion de constantes
    Ra = 10
    Ea = 350
    La = 100e-3
    kb = 7
    ki = 5
    Jm = 80
    bm = 20
    Torque = 0
#Declaracion de funciones y variables a trabajar
    i,w,theta,t = sp.symbols('i w theta t');
    #Corriente de armadura di(t)/dt
    f = sp.sympify(Ea/La - (Ra/La)*i - (kb/La)*w)
    #aceleracion angular del motor dw/dt
    g = sp.sympify((ki/Jm)*i - (bm/Jm)*w - Torque/Jm)
    #Velocidad angular del motor dtheta/dt
    h = sp.sympify(w)


#Metodos a utilizar
    f_euler,g_euler,h_euler, t_euler=euler([0,3],None,0,0,0,i,w,theta,t,f,g,h,0.5)
    sol_heun, t_heun = heun([0,3],None,0,0,0,i,w,theta,t,f,g,h,0.5)
    sol_rk4, t_rk4 = rungeKutta([0,3],None,0,0,0,i,w,theta,t,f,g,h,0.5)

#Escritura en el archivo .xlsx
    #Declaración de los DataFrame
    df_euler=pd.DataFrame({"x":f_euler,"y":g_euler,"z":h_euler})
    #Escritura
    with pd.ExcelWriter('Salida.xlsx') as writer:
        df_euler.to_excel(writer, sheet_name="Euler Method", index=False)

#Modulos para graficar
    path = "/home/leonardomadriz/Universidad/Apuntes/TercerAño/CT3233-PotenciaI/Proyecto/Codigo/phaseTwo/grafica/Salida_Euler"
    graf(t_euler,f_euler,"Euler",path,"Corriente vs Tiempo")
    graf(t_euler,g_euler,"Euler",path,"Velocidad angular vs Tiempo")
    graf(t_euler,h_euler,"Euler",path,"Posición angular vs Tiempo")


    graf(t_heun,[sublst[0] for sublst in sol_heun],"Heun",path,"Corriente vs Tiempo")
    graf(t_heun,[sublst[1] for sublst in sol_heun],"Heun",path,"Velocidad angular vs Tiempo")
    graf(t_heun,[sublst[2] for sublst in sol_heun],"Heun",path,"posición angular vs Tiempo")


    graf(t_rk4,[sublst[0] for sublst in sol_rk4],"RK4",path,"Corriente vs Tiempo")
    graf(t_rk4,[sublst[1] for sublst in sol_rk4],"RK4",path,"Corriente vs Tiempo")
    graf(t_rk4,[sublst[2] for sublst in sol_rk4],"RK4",path,"Corriente vs Tiempo")
if __name__ == "__main__":
    run()
