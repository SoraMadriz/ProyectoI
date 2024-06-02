import matplotlib.pyplot as plt
def grafError(value1,value2,value3,name):
#Datos del problema
    valores = [value1,value2,value3]
    colores = ['red', 'blue', 'green'] #Colores de las barras
    etiquetas = ['Euler', 'Heun', 'RK4'] #Etiquetas de las barras

# Crear la gráfica de barras
    plt.figure(figsize=(8, 6))
    plt.margins(x=0.1, y=0.1)
    plt.bar(etiquetas, valores, color=colores)

#Funciones a graficar y guardado
    plt.xlabel('Pasos')
    plt.ylabel('Error absoluto promedio')
    plt.savefig(f'/home/leonardomadriz/presentacion/{name}.png',dpi=300)
