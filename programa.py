#from funciones import *
from funciones import B2Decimal,Evaluar,OrdCromosomas,genmut
import random

while(True):
    try:
        numCromosomas = 2#int(input("Ingrese el numero de cromosomas: 2^"))
        numGenes = 3#int(input("Ingrese el numero de genes: 2^"))
        genesAMutar = 2#int(input("Ingrese el numero de genes que van a mutar: "))
        nGeneraciones = 8#int(input("Ingrese el numero de generaciones por las que van a mutar los genes: "))

        if genesAMutar<=(2**numGenes):
            break

        print("El numero de genes a mutar no puede igual o ser mayor a la cantidad de genes")

    except Exception as e:
        print("ingrese un valor valido")

tipoDeMutacion = random.randint(0,2)

mut = ""

mut = genmut(tipoDeMutacion)


Generaciones = []
Generacion = []
Cromosomas = []
Cromosoma = []
Genes = []

for i in range(2**numCromosomas):

    #Se generan de manera aleatoria los genes
    Genes = []
    valor = 2**(numGenes-2)
    for j in range(2**numGenes):
        Genes.append(random.randint(0,1))
    
    Cromosoma = []

    Cromosoma.append(Genes)
    Cromosoma.append(B2Decimal(Genes,numGenes)) # type: ignore
    Cromosoma.append(Evaluar(B2Decimal(Genes,numGenes))) # type: ignore
    
    Cromosomas.append(Cromosoma)

Generacion.append(OrdCromosomas(Cromosomas)) # type: ignore
Generacion.append(mut)

Generaciones.append(Generacion)



#Generaciones[
#   Generacion1[
#       Cromosomas[
#           Cromosoma1[
#               Genes[],
#               Decimal,
#               valor
#           ],
#           ...,
#           CromosomaX
#       ],
#       mut
#   ],
#   ...,
#   GeneracionX[]
#]

            # Generacion[0] = Cromosomas
            # Generacion[0][x] = Cromosomax
            # Generacion[0][0][j] = Genes #j
            # Generacion[0][0][0][i] = Gen en la poscicion i  
for g in Generaciones:
    for cromosoma in g[0]:
        print(cromosoma)

    print(g[1])

mut = Generaciones[0][1]
for g in range(nGeneraciones):

    if mut == "aleatorio":
        n = len(Generacion[0])
        combAleatoria = random.sample(range(n), n)
        for i in range(int(n/2)):
            for j in range(1,genesAMutar+1):
                x = combAleatoria[i]
                y = combAleatoria[n-i-1]
                Generacion[0][x][0][j], Generacion[0][y][0][j] = Generacion[0][y][0][j], Generacion[0][x][0][j]
    
    elif mut == "M con M":
        n = len(Generacion[0])
        i2 = 0
        i3 = 1
        for i in range (int(n/2)):
            for j in range(1,genesAMutar+1):
                Generacion[0][i2][0][j], Generacion[0][i3][0][j] = Generacion[0][i3][0][j], Generacion[0][i2][0][j]
            i2 += 2
            i3 += 2

    elif mut == "M con P":
        n = len(Generacion[0])
        for i in range(int(n/2)):
            for j in range(1,genesAMutar+1):
                Generacion[0][i][0][j], Generacion[0][n-i-1][0][j] = Generacion[0][n-i-1][0][j], Generacion[0][i][0][j]
    
    else:
        print("No se realizo ninguna mutacion")
        print(f"mut: {mut}")

    for cromos in Generacion[0]:
        cromos[1] = B2Decimal(cromos[0],numGenes)
        cromos[2] = Evaluar(cromos[1])
        
    Generacion[0] = OrdCromosomas(Generacion[0])

    tipoDeMutacion = random.randint(0,2)
    mut = genmut(tipoDeMutacion)
    Generacion[1] = mut
    #Se genera un nuevo tipo de mutacion

    Generaciones.append(Generacion) #Guarda la generacion mutada en la lista de generaciones



i = 0
for Gene in Generaciones:
    #Gene[0] = Cromosomas
    print()
    print(f"Generacion #{i+1}")
    
    for cromosoma in Gene[0]:
        print(cromosoma)
    
    i += 1
    if i < len(Generaciones):
        print(f"tipo de mutacion: {Gene[1]}")



