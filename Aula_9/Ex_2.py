'''Escreva um algoritmo que leia um valor para X e uma sub-rotina que imprima todos os números ímpares do intervalo fechado de 1 a X.
'''

def imprime_intervalo(y):
    i = 1
    while i <= y:
        if(i%2 == 1):
            print(i)
        i = i + 1

x = int(input("Informe um valor para X: "))
imprime_intervalo(x)