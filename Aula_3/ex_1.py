'''Faça um algoritmo que lê 10 valores para uma variável do tipo lista de nome x e mostre os 10 valores armazenados.'''

x = []

for a in range(1, 5):
    aux1 = int(input(f'Informe valor par x[{a}]: '))
    x.append(aux1)


for a in range(1, 5):
    print(f"X[{a}] = {x[a]}")
