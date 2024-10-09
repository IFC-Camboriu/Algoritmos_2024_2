'''Faça um algoritmo que lê uma matriz M5x5 e mostrar os valores da diagonal principal.'''

N = 3
matriz = []

# Inserindo dados na matriz usando for através da linha.
for l in range(N):
    linha = []
    for c in range(N):
        linha.append(int(input("Informe valores para a matriz: ")))
    matriz.append(linha)
    print(linha)

for i in range(N):
    print(f"Matriz(Diagonal)[{i}][{i}] = {matriz[i][i]}")
