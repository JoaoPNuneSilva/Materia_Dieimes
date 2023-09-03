import numpy as np
matriz = np.array([['Homem-Aranha -', 'Batman -', 'O Justiceiro'],
                   ['Deadpool -', 'Wolverine -', 'Superman'],
                   ['Flash -', 'Rorcharch -', 'Constantine']])
for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()