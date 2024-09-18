'''Faça um algoritmo que lê 10 valores para uma variável do tipo lista de nome x e mostre os 10 valores armazenados.'''

x = [0, 0, 0, 0, 0]

for a in range(0, len(x)):
    x[a] = int(input(f"Informe valor par x[{a}]: "))


for a in range(0, len(x)):
    print(f"X[{a}] = {x[a]}")