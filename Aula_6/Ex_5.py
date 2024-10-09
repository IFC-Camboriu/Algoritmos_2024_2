'''Faça um algoritmo que lê valores para uma matriz M10x10 calcular e mostrar:
O somatório dos valores da coluna 2
O somatório dos valores da diagonal principal
'''
N = 10
matriz = []
soma_col_2 = 0
soma_diagonal_prin = 0
# Inserindo dados na matriz usando for através da linha.
for l in range(N):
    linha = []
    for c in range(N):
        linha.append(int(input("Informe valores para a matriz")))
    matriz.append(linha)
    print(linha)

print(f"Matriz {N}x{N}: ", matriz)

for l in range(N):
    soma_col_2 = soma_col_2 + matriz[l][2]

print(soma_col_2)

for i in range(N):
    soma_diagonal_prin = soma_diagonal_prin + matriz[i][i]

print(soma_diagonal_prin)