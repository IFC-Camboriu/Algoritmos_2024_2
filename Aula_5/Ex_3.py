'''Faça um algoritmo que lê estrutura (lista, tupla ou conjunto), K que comporte 20 elementos. Troque a seguir os elementos de índice ímpar com os de índice par imediatamente seguinte mostre no final como ficou a estrutura K, com as alterações.
'''

K =[]
i = 0
aux = 0

while i < 20:
    valor_K = int(input(f'Digite o {i + 1}° para adicionar à estrutura K:  '))
    K.append(valor_K)
    i += 1

print(K)

i = 1 #inicializa novamnete para evitar que o valor de i se mantenha em 20

while i < len(K):
    if i == len(K) - 1:
        break
    else:
        aux = K[i]
        K[i] = K[i+1]
        K[i+1] = aux
    i = i + 2

print(K)