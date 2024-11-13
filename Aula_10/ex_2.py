'''Faça uma sub-rotina que receba como parâmetro uma matriz(lista de lista) A[5][5] e retorne a soma de todos os seus elementos.'''

def soma_matriz (matriz):
    soma = 0
    for l in range(len(matriz)):
        for c in range(len(matriz)):
            soma = soma + matriz[l][c]
    return soma

mat = []
cont = 0
N = 4
# preenche a matriz
for l in range(N):
    aux = []
    for c in range(N):
        aux.append(cont)
        cont = cont + 1
    mat.append(aux)

print(mat)

print(f"A soma da matriz é {soma_matriz(mat)}")