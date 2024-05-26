import matplotlib.pyplot as plt

def graf(axis1,axis2,method):
    fig,ax=plt.subplots();
    ax.grid(True)
    ax.set_title("Function")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.plot(axis1,axis2, color="red", label=method)
    ax.legend(loc="upper right")
    plt.show()
