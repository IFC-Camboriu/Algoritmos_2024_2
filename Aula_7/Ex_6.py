# Faça um programa que leia um vetor(lista) de 5 posições e uma matriz de 5 x 5 calcule e 
# mostre o resultado da multiplicação do primeiro elemento do vetor, por toda a 
# primeira linha da matriz, do segundo item do vetor por toda a segunda linha da 
# matriz e assim sucessivamente.

lista = []
listav = []

# fazendo a leitura da lista(vetor) com 5 elementos
for z in range(5):
    listav.append(int(input("Digite um número para lista:")))

matriz = []

#faz a leitura dos elementos da matriz
for l in range(5):
    lista = []
    for c in range(5):
        lista.append(int(input("Digite um valor: ")))
    matriz.append(lista)

# exibe os valores armazenados na matriz
print("Matriz 5 por 5:")
for p in matriz:
    print(p)
# exibe os valores armazenados na lista(vetor)
print("Lista:",listav)

# realiza a multiplicação de cada elemento do vetor por todos os elementos de uma linha da matriz
for s in range(5):
    for j in range(5):
        matriz[s][j] = matriz[s][j] * listav[s]

#exibe os valores multiplicados outra forma de exibir os valores com fatiamento
'''print("Teste")
print(matriz[:][:])'''

print("Resultado:")
for sas in matriz:
    print(sas)

