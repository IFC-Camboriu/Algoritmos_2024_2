'''Faça um algoritmo que lê uma matriz M5x5. Calcular e mostrar a soma de todos os valores da linha 4.'''
matriz = []
soma = 0
N = 5
# Inserindo dados na matriz usando for através da linha.
for l in range(N):
    linha = []
    for c in range(N):
        linha.append(int(input("Informe valores para a matriz: ")))
    matriz.append(linha)
    print(linha)

print("Matriz 5x5: ", matriz)

for c in range(N):
    soma = soma + matriz[4][c]

print(f"O valor da soma da linha 4 é: {soma}")