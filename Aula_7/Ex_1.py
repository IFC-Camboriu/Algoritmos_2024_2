'''Faça um algoritmo que receba um valor N correspondente ao tamanho de duas matrizes quadradas de ordem N (NxN).
 Leia os valores inteiros para preencher todas as posições de cada uma das matrizes, e calcule a SOMA das matrizes.'''
# Lembrando que o tamanho da matriz foi reduzido para 3x3 para que não seja preciso ficar digitando vários valores para testar na aula

matrizA = []
matrizB = []
resultado = []

n = int(input("Informe o tamanho da matriz: "))

#preenche A
for l in range(n):
    linha = []
    for c in range(n):
        linha.append(int(input("Informe valores para a matriz A: ")))
    matrizA.append(linha)
#preenche B
for l in range(n):
    linha = []
    for c in range(n):
        linha.append(int(input("Informe valores para a matriz B: ")))
    matrizB.append(linha)

print("Matriz A: ", matrizA)
print("Matriz B: ", matrizB)

# combinando o uso do append com a soma percorrendo os índices da matriz A e da Matriz B
for l in range(n):
    linha = []
    for c in range(n):
        linha.append(matrizA[l][c] + matrizB[l][c])
    resultado.append(linha)

print("Matriz Resultado: ", resultado)