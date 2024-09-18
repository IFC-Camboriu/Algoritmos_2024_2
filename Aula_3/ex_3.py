'''3 - Elabore um algoritmo que leia duas listas de 5 posições, após a leitura realizar a soma e imprima o resultado da soma entre as duas listas de inteiros.
'''

L1 = []
L2 = list()
L3 = list()

for x in range(0, 5):
    aux1 = int(input(f'Informe valor par L1[{x}]'))
    L1.append(aux1)

for x in range(0, 5):   
    aux2 = int(input(f'Informe valor par L2[{x}]'))
    L2.append(aux2)

print(L1)
print(L2)

for k in range(0, len(L1)):
    aux1 = L1[k] + L2[k]
    L3.append(aux1)

print(L3)