from sys import exit
def calError(time1,time2,v_real,v_appx,mark):
    output=[]
    j=None

    if mark == "c":
        j=0
    elif mark == "w":
        j=1
    elif mark == "t":
        j = 2
    for i in range(len(time1)):
        if int(time1[i]) != int(time2[i]):
            print("Condición no cumplida")
            exit()
        else:
         error_abs=abs(v_real[i] - v_appx[i][j])
         print(error_abs)
         output.append(error_abs)
    return output
