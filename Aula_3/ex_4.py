'''4 - Altere o algoritmo anterior para que ele realize o
 produto da primeira lista, pelo inverso da segunda lista.
'''

L1 = []
L2 = list()
L3 = list()

for x in range(0, 5):
    aux1 = int(input(f'Informe valor par L1[{x}]'))
    L1.append(aux1)
    aux2 = int(input(f'Informe valor par L2[{x}]'))
    L2.append(aux2)

print(L1)
print(L2)

for x in range(0, len(L1)):
    aux1 = L1[x] * L2[len(L2) - 1 - x]
    L3.append(aux1)

print(L3)