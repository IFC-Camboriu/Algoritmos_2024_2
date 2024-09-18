'''Faça um algoritmo que lê 10 valores para uma variável do tipo lista de nome x. 
Após completar toda a leitura da lista, verificar se cada valor armazenado na lista é par ou ímpar.
Se for par, fazer com que o valor seja atualizado para o resultado da multiplicação do valor contido pelo índice. 
Se for impar fazer com que a lista receba o valor do seu próprio índice.'''

x = []
y = 0

for a in range(0, 10): # atribui valores
   x.append(int(input(f'Informe valor par x[{a}]: ')))

while(y < len(x)): # verificação se é par ou impar
    if(x[y] % 2 == 0):
        x[y] = x[y] * y
    else:
        x[y] = y
    y = y + 1 # controle do laço

print(x)