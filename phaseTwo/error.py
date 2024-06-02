from sys import exit
import matplotlib.pyplot as plt
def calError(time1,time2,v_real,v_appx,mark,method,check,h):
    output=[]
    j=None
    promedio = []

    if mark == "c":
        j=0
    elif mark == "w":
        j=1
    elif mark == "t":
        j = 2
    for i in range(len(time1)):
        error_abs=abs(v_real[i] - v_appx[i][j])
        output.append(error_abs)

    if check == True:
        promedio = sum(output)/len(output)
    return output, promedio
