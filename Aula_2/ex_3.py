'''Faça um algoritmo que lê 5 valores para uma variável do tipo vetor  e determine a média de todos valores armazenados no vetor.'''

import numpy as np

soma = 0
# tamanho do array
N = 5

#preenche a estrutura com zeros
x = np.zeros(N, dtype=int)

#preenche o x com valores do tipo float
for i in range(N):
    x[i] = float(input(f'Informe um valor para V[{i}]: '))
    soma = soma + x[i]

print(soma/N)