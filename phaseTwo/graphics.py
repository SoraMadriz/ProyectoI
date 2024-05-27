#Dependencias del modulo
import matplotlib.pyplot as plt                # Función de gráficas
import os                                      # Manejo del sistema
#-----------------------Entrada y Salida del Modulo-----------------------------
# Entrada: eje de las abscisas    -->  (axis1)
#          eje de las ordenadas   -->  (axis2)
#          nombre del método      -->  (method)
#          dirección de guardado  -->  (path)
#          Nombre de la grafica   -->  (name)
def graf(axis1,axis2,method,path,name):
    fig,ax=plt.subplots()

#Ajuste en las cuadriculas
    ax.grid(True)

#Etiquetas de la gráfica
    ax.set_title(name)
    ax.set_xlabel("x")
    ax.set_ylabel("y")

#Funciones a graficar y guardado
    ax.plot(axis1,axis2, marker="o",color="red", label=method)
    ax.legend(loc="upper right")
    plt.savefig(f'{path}/{name}.png')
    plt.show()
