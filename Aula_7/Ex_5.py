#Faça um algoritmo que lê uma matriz M2X2 que calcula e mostra o resultado do determinante
# desta matriz.

x = [[], []]

# Insere valores na matriz
for index, linha in enumerate(x):
  for c in range(len(x)):
    linha.append(int(input(f'Digite o {c + 1}o valor para a linha {index + 1}: ')))

# Definição das diagonais (principal/secundária)
dp = 1
ds = 1

# Multiplicação das diagonais
'''for c in range(len(x)):
  dp *= x[c][c]
  ds *= x[c][-(c+1)]'''

# Multiplicação das diagonais
dp = x[0][0] * x[1][1]
ds = x[0][1] * x[1][0]

# Print matriz
print('\nMATRIZ: ')
for linha in x:
  print(linha)

# Resultado determinante
print(f'Determinante: {dp - ds} ')