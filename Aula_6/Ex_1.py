'''Faça um algoritmo que lê uma matriz M5x5 e mostrar os valores digitados para a matriz M.'''
# Lembrando que o tamanho da matriz foi reduzido para 3x3 para que não seja preciso ficar digitando vários valores para testar na aula
N = 3
matriz = []

# Inserindo dados na matriz usando for através da linha.
for l in range(N):
    linha = []
    for c in range(N):
        linha.append(int(input("Informe valores para a matriz: ")))
    matriz.append(linha)
    print(linha)

print(f"Matriz {N}x{N}: ", matriz)