
def B2Decimal(arreglo, numGenes):
    decimal = 0
    signo = 1
    for i in range(len(arreglo)):
        if i == 0:
            if arreglo[i] == 1:
                signo = -1
        elif i == len(arreglo):
            if arreglo[i] == 1:
                decimal += 0.5
        else:
            if arreglo[i] == 1:
                decimal += 2**((2**numGenes)-2-i)
    return decimal*signo

def Evaluar(datos):
    #Poner la funcion que se va a utilizar para la evaluacion
    return datos**2 +2

def OrdCromosomas(Cromosomas):
    # for i in range(len(Cromosomas)):
    #     for j in range(0, len(Cromosomas)-i-1):
    #         if Cromosomas[j][2] > Cromosomas[j+1][2]:
    #             Cromosomas[j], Cromosomas[j+1] = Cromosomas[j+1], Cromosomas[j]
    
    # return Cromosomas

    return sorted(Cromosomas, key=lambda cromosoma: cromosoma[2])


def genmut(tipoDeMutacion):
    mut = ""
    if tipoDeMutacion == 0:
        # print("El tipo de mutación es aleatorio")
        mut = "aleatorio"
    elif tipoDeMutacion == 1:
        # print("El tipo de mutacion es de mejor con mejor")
        mut = "M con M"
    elif tipoDeMutacion == 2:
        # print("El tipo de mutacion es de mejor con peor")
        mut = "M con P"
    return mut