'''1.Faça uma sub-rotina que recebe duas listas A e B com dez
elementos inteiros como parâmetro. A sub-rotina deverá determinar
e mostrar o vetor C que contém os elementos que estão em A, mas
que não estão em B. A lista C deverá ser mostrada no programa
principal.'''

def diferenca(a, b):
    
    for i in range(0,len(a)):
        flag = 0
        for j in range(0,len(b)):
            if(a[i] == b[j]):
                flag = 1
        if(flag == 0):
            c.append(a[i])



a = [8, 9, 3, 4, 5]
b = [1, 2, 3, 4, 5, 6]
c = []
diferenca (a, b)

print(c)