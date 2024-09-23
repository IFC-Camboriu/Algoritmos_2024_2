'''Faça um programa que preencha dois vetores, X e Y, com dez números inteiros cada. Calcule e mostre os seguintes vetores resultantes:
A diferença entre X e Y
'''
x = []
y = []
dif = []
cont = 0
for i in range(0,5):
    x.append(int(input(f"Informe um valor para a posição {i}: ")))

for i in range(0,5):
    y.append(int(input(f"Informe um valor para a posição {i}: ")))

'''for i in range(0,5): # indice de x
    for j in range(0,5): # indice de y
        if(x[i] == y[j]):
            break
        if(x[i] != y[j]):
            cont = cont + 1
    if(cont == 5) and (x[i] not in dif):
        dif.append(x[i])
    cont = 0'''

for i in x:
    if(i not in y) and (i not in dif):
        dif.append(i)



print(dif)