'''Crie uma sub-rotina que receba como parâmetro uma lista V contendo 25 elementos 
de números inteiros e substitua todos os valores negativos de V por 0. A lista deverá ser retornada para quem realizou a chamada desta função.
'''
def verica_valores(V):
    for i in range(0, len(V)):
        if(V[i] < 0):
            V[i] = 0

lista = []

for i in range(-5, 5):
    lista.append(i)

print(lista)

verica_valores(lista)

print(lista)