import matplotlib.pyplot as plt

# Datos de ejemplo
valores = [0.0009353138910545984,7.912171567535564e-08,3.306079409729604e-08]  # Valores de las barras
colores = ['red', 'blue', 'green']  # Colores de las barras
etiquetas = ['Euler', 'Heun', 'RK4']  # Etiquetas de las barras

# Crear la gráfica de barras
plt.bar(range(len(valores)), valores, color=colores)

# Añadir los valores encima de las barras en forma de porcentaje
for i in range(len(valores)):
    porcentaje = str(round(valores[i],2))
    plt.text(i, valores[i] + 1, porcentaje, ha='center')

# Añadir las etiquetas del eje x
plt.xticks(range(len(valores)), etiquetas)

# Mostrar la gráfica
plt.show()
