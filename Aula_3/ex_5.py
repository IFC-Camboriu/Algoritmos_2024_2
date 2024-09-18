'''Faça um algoritmo que lê duas listas A e B com 5 elementos  cada. Construir uma lista C, sendo este a junção das duas  outras listas, ou seja, a lista C deverá conter 10 elementos. Mostre no final a lista C'''

A = []
B = list()
C = [0,0,0,0,0,0,0,0,0,0]

for x in range(0, 5):
    aux1 = int(input(f'Informe valor par A[{x}]'))
    A.append(aux1)

for x in range(0, 5):
    aux2 = int(input(f'Informe valor par B[{x}]'))
    B.append(aux2)

print(A)
print(B)

#C = A + B

for y in range(0, 5):
    C[y] = A[y]
    C[y + 5] = B[y]

#for y in range(0, 5):
    

print(C)