'''Escreva um algoritmo que imprima todos os números inteiros de 10 a 1 (em ordem decrescente), utilizando recursividade.'''

def ordem_desc(y):
    print(y)
    if(y != 1):
        ordem_desc(y - 1)
    

x = 10
ordem_desc(x)
