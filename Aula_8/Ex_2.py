'''Faça um algoritmo contendo uma sub-rotina 
que receba dois números positivos inteiros 
por parâmetro e retorne a soma dos N números
 inteiros existentes entre eles, incluindo 
 na soma os dois números informados.
'''
def soma_valores(m, n):
    soma = 0
    i = m
    while(i <= n):
        soma = soma + i
        i = i + 1
    return soma

x = int(input("Informe o primeiro número: "))
y = int(input("Informe o segundo número: "))

if(x < 0 or y < 0):
    print("Valores Informado é negativo!")
elif(x > y):
    resultado_soma = soma_valores(y, x)
else:
    resultado_soma = soma_valores(x, y)

print(resultado_soma)