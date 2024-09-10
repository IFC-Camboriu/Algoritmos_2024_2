'''Faça um algoritmo que lê 10 valores para uma variável do tipo vetor de nome x e mostra os 10 valores armazenados na estrutura.'''
import numpy as np

# tamanho do array
N = 10

#preenche a estrutura com zeros e com o tipo inteiro
x = np.zeros(N, dtype=int)

print(x)

#preenche o x com valores do tipo float
for i in range(N):
    x[i] = float(input(f'Informe um valor para V[{i}]: '))

print(x)