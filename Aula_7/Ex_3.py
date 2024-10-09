# Faça um algoritmo que lê valores para uma matriz M4X4 e um valor para a variável “a” 
# (do tipo simples, pode ser: inteiro, float). Multiplicar cada valor contido na matriz
# pelo valor da variável e colocar os resultados num vetor(lista) V com 16 elementos. 
# Mostre no final o vetor(lista).

matriz = []
v = []

# faz a leitura da matriz
for l in range(4):
    lista = []
    for c in range(4):
        lista.append(float(input("Digite um valor: ")))
    matriz.append(lista)

#mostra a matriz
print("Matriz 4 por 4:")
for p in matriz:
    print(p)

# faz a leitura da variavel
a = float(input("Digite um número para variável ""a"": "))

# realiza a multiplicação e salva em v
for p in range(4):
    for n in range(4):
        aux = matriz[p][n] * a
        v.append(float(aux))

#mostra a lista resultante
print("Resultado:",v)