# Importación de modulos requeridos para trabajar
import numpy as np                   #Trabajo con matrices
import matplotlib.pyplot as plt      #Graficas
import pandas as pd                  #Manejo de datos
import sympy as sp                   #Matemática simbólica
from time import time                #Tiempo
import psutil                        #Estado de la computadora
from warnings  import filterwarnings #Manejos de mensajes
from scipy.integrate import odeint   # Equivalente a isode
from isode import isopy              #Subprocesos
from Euler import euler              #Metodo de Euler
from Heun import heun                #Metodo de Heun
from RK4 import rungeKutta           #Metodo de RK4
from graphics import graf            #Graficar salida de los metodos
from error import calError           #Calculo de errores
from grafierror import grafError     #Grafica de error
from sys import exit

def run():
#Declaracion de constantes y variables
    #Constantes mecánicas
    kb = 7; ki = 5; Jm = 80; bm = 20; Tl = 14#Uso de w
    #Constantes eléctricas
    Ra=10; Ea = 350; La = 100e-3
    #Variables de metodos
    step = 0.001; rank=[0,3]
    #variables de almacenamiento
    file1 = "5.Corridas"; file2 = "Escenario1"
    #Variables de proceso
    check = False

#Declaracion de funciones y variables a trabajar
    i,w,theta,t = sp.symbols('i w theta t')
    #Condicion impuesta
    if Tl is None:
        Tl = 0.3*(w**2)
    #Corriente de armadura di(t)/dt
    f = sp.sympify(Ea/La - (Ra/La)*i - (kb/La)*w)
    #aceleracion angular del motor dw/dt
    g = sp.sympify((ki/Jm)*i - (bm/Jm)*w - Tl/Jm)
    #Velocidad angular del motor dtheta/dt
    h = sp.sympify(w)

#Obtencion de la solucion teorica
    isode_result, isode_time = isopy(Ra, Ea, La, kb, ki, Jm, bm, Tl,step,None,rank)

#Metodos a utilizar
    #Metodo de Euler
    start = time()
    f_euler,g_euler,h_euler, t_euler, cpu_euler = euler(rank,None,0,0,0,i,w,theta,t,f,g,h,step)
    end = time()
    duration_euler = end - start

    #Metodo de Heun
    start = time()
    sol_heun, t_heun, cpu_heun = heun(rank,None,0,0,0,i,w,theta,t,f,g,h,step)
    end = time()
    duration_heun = end - start

    #Metodo de RK4
    start = time()
    sol_rk4, t_rk4,cpu_rk4 = rungeKutta(rank,None,0,0,0,i,w,theta,t,f,g,h,step)
    end = time()
    duration_rk4 = end - start

#Calculo de errores
    #Euler
    error_euler_i, euler_promi = calError(t_euler,isode_time,f_euler,isode_result,"c","Euler",check,step) #Corriente
    error_euler_w, euler_promw = calError(t_euler,isode_time,g_euler,isode_result,"w","Euler",check,step) #Velocidad angular
    error_euler_t, euler_promt = calError(t_euler,isode_time,h_euler,isode_result,"t","Euler",check,step) #Posicion angular

    #Heun
    #Funciones de heun
    hi = [sublst[0] for sublst in sol_heun]
    hw = [sublst[1] for sublst in sol_heun]
    htheta = [sublst[2] for sublst in sol_heun]
    #Calculo de errores
    error_heun_i, heun_promi= calError(t_euler,isode_time,hi,isode_result,"c","Heun",check,step)     #Corriente
    error_heun_w, heun_promw = calError(t_euler,isode_time,hw,isode_result,"w","Heun",check,step)     #Velocidad angular
    error_heun_t, heun_promt = calError(t_euler,isode_time,htheta,isode_result,"t","Heun",check,step) #Posicion angular

    #rk4
    #Funciones de heun
    ri = [sublst[0] for sublst in sol_rk4]
    rw = [sublst[1] for sublst in sol_rk4]
    rtheta = [sublst[2] for sublst in sol_rk4]
    #Calculo de errores
    error_rk4_i, rk4_promi = calError(t_rk4,isode_time,ri,isode_result,"c","RK4",check,step)     #Corriente
    error_rk4_w, rk4_promw = calError(t_rk4,isode_time,rw,isode_result,"w","RK4",check,step)     #Velocidad angular
    error_rk4_t, rk4_promt = calError(t_rk4,isode_time,rtheta,isode_result,"t","RK4",check,step) #Posicion angular
    

#Modulos para graficar
    #Metodo de ISODE
    if check == False:
        path = f'./presentacion/{file1}/{file2}/Salida_Isode'
        graf(isode_time,[sublst[0] for sublst in isode_result],"ISODE",path,"Corriente vs Tiempo")
        graf(isode_time,[sublst[1] for sublst in isode_result],"ISODE",path,"Velocidad angular vs Tiempo")
        graf(isode_time,[sublst[2] for sublst in isode_result],"ISODE",path,"Posición angular vs Tiempo")

    #Metodo de Euler
        path = f'./presentacion/{file1}/{file2}/Salida_Euler'
        graf(t_euler,f_euler,"Euler",path,"Corriente vs Tiempo")
        graf(t_euler,g_euler,"Euler",path,"Velocidad angular vs Tiempo")
        graf(t_euler,h_euler,"Euler",path,"Posición angular vs Tiempo")

    #Metodo de Heun (Euler Mejorado)
        path = f'./presentacion/{file1}/{file2}/Salida_Heun'
        graf(t_heun,hi,"Heun",path,"Corriente vs Tiempo")
        graf(t_heun,hw,"Heun",path,"Velocidad angular vs Tiempo")
        graf(t_heun,htheta,"Heun",path,"Posición angular vs Tiempo")

    #Metodo de RK4
        path = f'./presentacion/{file1}/{file2}/Salida_RK4'
        graf(t_rk4,ri,"RK4",path,"Corriente vs Tiempo")
        graf(t_rk4,rw,"RK4",path,"Velocidad angular vs Tiempo")
        graf(t_rk4,rtheta,"RK4",path,"Posición angular vs Tiempo")

    #Grafica de errores
    elif check == True:
        grafError(euler_promi,heun_promi,rk4_promi,f'{file1}_corriente_{step}')
        grafError(euler_promw,heun_promw,rk4_promw,f'{file1}_velocidadAngular_{step}')
        grafError(euler_promt,heun_promt,rk4_promt,f'{file1}_posicionAngular_{step}')
        exit()


#Escritura de los errores absolutos
    #Euler
    df_euler=pd.DataFrame({"TIEMPO":t_euler,
                           "CORRIENTE":f_euler,
                           "VEL. ANGULAR":g_euler,
                           "POS. ANGULAR":h_euler})

    #Heun
    df_heun=pd.DataFrame({"TIEMPO":t_heun,
                           "CORRIENTE":hi,
                           "VEL. ANGULAR":hw,
                            "POS. ANGULAR":htheta})

    #RK4
    df_rk4=pd.DataFrame({"TIEMPO":t_rk4,
                           "CORRIENTE":ri,
                           "VEL. ANGULAR":rw,
                           "POS. ANGULAR":rtheta})
    with pd.ExcelWriter(f'./presentacion/{file1}/{file2}/Solucion.xlsx') as writer:
        df_euler.to_excel(writer, sheet_name="Euler Method", index=False)
        df_heun.to_excel(writer, sheet_name="Heun Method", index=False)
        df_rk4.to_excel(writer, sheet_name="RK4 Method", index=False)

#Escritura de la solucion
    #Euler
    df_euler=pd.DataFrame({"TIEMPO":t_euler,
                           "CORRIENTE":error_euler_i,
                           "VEL. ANGULAR":error_euler_w,
                           "POS. ANGULAR":error_euler_t})

    #Heun
    df_heun=pd.DataFrame({"TIEMPO":t_heun,
                           "CORRIENTE":error_heun_i,
                           "VEL. ANGULAR":error_heun_w,
                            "POS. ANGULAR":error_heun_t})

    #RK4
    df_rk4=pd.DataFrame({"TIEMPO":t_rk4,
                           "CORRIENTE":error_rk4_i,
                           "VEL. ANGULAR":error_rk4_w,
                           "POS. ANGULAR":error_rk4_t})
    with pd.ExcelWriter(f'./presentacion/{file1}/{file2}/ErrorAbsoluto.xlsx') as writer:
        df_euler.to_excel(writer, sheet_name="Euler Method", index=False)
        df_heun.to_excel(writer, sheet_name="Heun Method", index=False)
        df_rk4.to_excel(writer, sheet_name="RK4 Method", index=False)

#Recursos de los métodos
    state_variable = pd.DataFrame({
        'Métodos empleados':['Euler','Heun','RK4'],
        'Duración':[duration_euler,duration_heun,duration_rk4],
        'CPU' : [cpu_euler[0],cpu_heun[0],cpu_rk4[0]],
        'RAM' : [cpu_euler[1],cpu_heun[1],cpu_rk4[1]]
    })
    #Tabla:
    filterwarnings("ignore", category=FutureWarning)
    table= state_variable.pivot_table(
        values=['Duración','CPU','RAM'],
        index='Métodos empleados',
        aggfunc=np.sum)
    print("FINAL DEL CALCULO")
    print("-"*40)
    print("\tVARIABLES DE ESTADO")
    print(table)

if __name__ == "__main__":
    run()
