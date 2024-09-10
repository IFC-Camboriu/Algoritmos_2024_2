'''Faça um algoritmo que lê 10 valores para uma variável do tipo vetor  e mostre qual a posição está armazenado o maior e o menor valor no vetor.
'''

import numpy as np

maior = 0
menor = 0
posi_maior = 0
posi_menor = 0
# tamanho do array
N = 5

#preenche a estrutura com zeros
x = np.zeros(N, dtype=int)

#preenche o x com valores do tipo float
for i in range(N):
    x[i] = float(input(f'Informe um valor para V[{i}]: '))

# determinar o maior e o menor elemento contido na estrutura
for y in range(N):
    if(y == 0):
        maior = x[y]
        menor = x[y]
    if (maior < x[y]):
        maior = x[y]
        posi_maior = y
    if (menor > x[y]):
        menor = x[y]
        posi_menor = y

print("O menor valor é",menor, "e está na posicao:", posi_menor)
print(f"O maior valor é {maior} e está na posicao:{posi_maior}")