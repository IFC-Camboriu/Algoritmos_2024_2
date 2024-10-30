'''Faça uma sub-rotina que imprima todos os 
números inteiros de 10 a 1 ( ou seja, em 
ordem decrescente).
'''

def decresce(x, y):
    for i in range(y, x - 1, -1):
        print(i)

decresce(1, 10)