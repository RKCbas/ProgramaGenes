#from funciones import *
from funciones import B2Decimal, Evaluar, OrdCromosomas, genmut
import random

while(True):
    try:
        numCromosomas = int(input("Ingrese el numero de cromosomas: 2^"))
        numGenes = int(input("Ingrese el numero de genes: 2^"))
        genesAMutar = int(input("Ingrese el numero de genes que van a mutar: "))
        nGeneraciones = int(input("Ingrese el numero de generaciones por las que van a mutar los genes: "))

        if genesAMutar <= (2**numGenes):
            break

        print("El numero de genes a mutar no puede igual o ser mayor a la cantidad de genes")

    except Exception as e:
        print("Ingrese un valor válido")

tipoDeMutacion = random.randint(0, 2)
mut = genmut(tipoDeMutacion)

# Inicialización de generaciones y cromosomas
Generaciones = []
Generacion = []
Cromosomas = []

for i in range(2**numCromosomas):
    # Se generan de manera aleatoria los genes
    Genes = []
    for j in range(2**numGenes):
        Genes.append(random.randint(0, 1))

    Cromosoma = []
    Cromosoma.append(Genes)
    Cromosoma.append(B2Decimal(Genes, numGenes))  # type: ignore
    Cromosoma.append(Evaluar(B2Decimal(Genes, numGenes)))  # type: ignore

    Cromosomas.append(Cromosoma)


Generacion.append(Cromosomas)  # type: ignore
Generacion.append(mut)


for cromos in Generacion[0]:
    cromos[1] = B2Decimal(cromos[0], numGenes)
    cromos[2] = Evaluar(cromos[1])

# Ordenar los cromosomas por el valor evaluado
Generacion[0] = OrdCromosomas(Generacion[0])

# Clonar la generación actual (para evitar referencias) antes de agregarla a la lista de generaciones
nueva_generacion = [cromo.copy() for cromo in Generacion[0]]
Generaciones.append([nueva_generacion, mut])

# Imprimir la primera generación
# for g in Generaciones:
#     for cromosoma in g[0]:
#         print(cromosoma)
#     print(g[1])

# Algoritmo de mutación a través de generaciones
mut = Generaciones[0][1]
for g in range(nGeneraciones):
    # Aplicar mutación
    if mut == "aleatorio":
        n = len(Generacion[0])
        combAleatoria = random.sample(range(n), n)
        for i in range(int(n / 2)):
            for j in range(1, genesAMutar + 1):
                x = combAleatoria[i]
                y = combAleatoria[n - i - 1]
                Generacion[0][x][0][j], Generacion[0][y][0][j] = Generacion[0][y][0][j], Generacion[0][x][0][j]

    elif mut == "M con M":
        n = len(Generacion[0])
        i2 = 0
        i3 = 1
        for i in range(int(n / 2)):
            for j in range(1, genesAMutar + 1):
                Generacion[0][i2][0][j], Generacion[0][i3][0][j] = Generacion[0][i3][0][j], Generacion[0][i2][0][j]
            i2 += 2
            i3 += 2

    elif mut == "M con P":
        n = len(Generacion[0])
        for i in range(int(n / 2)):
            for j in range(1, genesAMutar + 1):
                Generacion[0][i][0][j], Generacion[0][n - i - 1][0][j] = Generacion[0][n - i - 1][0][j], Generacion[0][i][0][j]

    # Recalcular los valores de cada cromosoma
    for cromos in Generacion[0]:
        cromos[1] = B2Decimal(cromos[0], numGenes)
        cromos[2] = Evaluar(cromos[1])

    # Ordenar los cromosomas por el valor evaluado
    Generacion[0] = OrdCromosomas(Generacion[0])

    # Generar nuevo tipo de mutación
    tipoDeMutacion = random.randint(0, 2)
    mut = genmut(tipoDeMutacion)
    Generacion[1] = mut

    # Clonar la generación actual (para evitar referencias) antes de agregarla a la lista de generaciones
    nueva_generacion = [cromo.copy() for cromo in Generacion[0]]
    Generaciones.append([nueva_generacion, mut])


# Imprimir todas las generaciones
i = 0
for Gene in Generaciones:
    print()
    print(f"Generación #{i + 1}")
    
    for cromosoma in Gene[0]:
        print(cromosoma)

    i += 1
    if i < len(Generaciones):
        print(f"Tipo de mutación: {Gene[1]}")
