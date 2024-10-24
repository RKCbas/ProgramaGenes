import random
from funciones import *

numGenes = 3
genesAMutar = 2

Generacion = [
    [
        [
            [1, 0, 0, 1, 1, 0, 0, 1], 
            -12.5, 
            -12.5
        ], 
        [
            [0, 0, 1, 0, 0, 1, 0, 0], 
            18, 
            18
        ], 
        [
            [0, 0, 1, 0, 0, 1, 1, 0], 
            19, 
            19
        ], 
        [
            [0, 0, 1, 0, 1, 0, 1, 1], 
            21.5,
            21.5
        ]
    ],
    'M con M'
]
Generaciones = []
primgen = Generacion
Generaciones.append(primgen)
print()
for cromosoma in Generacion[0]:
    print(cromosoma)

print()
# n = len(Generacion[0])
# combAleatoria = random.sample(range(n), n)
# for i in range(int(n/2)):
#     for j in range(1,genesAMutar+1):
#         x = combAleatoria[i]
#         y = combAleatoria[n-i-1]
#         Generacion[0][x][0][j], Generacion[0][y][0][j] = Generacion[0][y][0][j], Generacion[0][x][0][j]

# for cromos in Generacion[0]:
#     cromos[1] = B2Decimal(cromos[0],numGenes)
#     cromos[2] = Evaluar(cromos[1])
    
# Generacion[0] = OrdCromosomas(Generacion[0])

# for cromosoma in Generacion[0]:
#     print(cromosoma)

for h in range(5):
    
    print(f"h: {h}")
    n = len(Generacion[0])
    combAleatoria = random.sample(range(n), n)
    for i in range(int(n/2)):
        for j in range(1,genesAMutar+1):
            x = combAleatoria[i]
            y = combAleatoria[n-i-1]
            Generacion[0][x][0][j], Generacion[0][y][0][j] = Generacion[0][y][0][j], Generacion[0][x][0][j]

    for cromos in Generacion[0]:
        cromos[1] = B2Decimal(cromos[0],numGenes)
        cromos[2] = Evaluar(cromos[1])
        
    Generacion[0] = OrdCromosomas(Generacion[0])

    

    Generaciones.append(Generacion)


for Genera in Generaciones:
    for cromosoma in Genera[0]:
        
        print(cromosoma)
    print(Genera[1])
    print()
