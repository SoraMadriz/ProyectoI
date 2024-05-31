import matplotlib.pyplot as plt

def graf(axis1,axis2,method):
    fig,ax=plt.subplots();
    ax.grid(True)
    ax.set_title("Function")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    if method == "Corriente vs Tiempo":
        curveColors = "darkorange"
    elif method =="Velocidad angular vs Tiempo":
        curveColors = "darkorchid"
    elif method =="Posición angular vs Tiempo":
        curveColors = "dodgerblue"
    ax.plot(axis1,axis2, color=curveColors, label=method)
    ax.legend(loc="upper right")
    plt.show()
