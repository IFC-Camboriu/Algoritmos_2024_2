'''Escreva um programa que preencha um vetor de inteiros de 10 posições e solicite ao usuário um valor inteiro para ser procurado no vetor. Crie uma função que receba como parâmetro o vetor e o número a ser procurado. Ao final, retorne quantas vezes o número foi encontrado no vetor.'''
N = 10

def quantidade_ocorrencias (v, valor):
    cont = 0
    for l in range(len(v)):
        if(v[l] == valor):
            cont = cont + 1
    return cont

vet = []
cont = 0
for i in range(N):
    vet.append(cont)
    cont = cont + 1

print(vet)

valor = int(input("Informe um valor para ser buscado "))

print(f"O valor {valor} aparece {quantidade_ocorrencias(vet, valor)} vez(es).")
