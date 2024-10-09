#Faça um algoritmo que lê uma matriz VIM10x10. Troque a seguir os valores contidos 
# na linha de índice 2 com os da linha de índice 8 e também troque os valores da 
# linha de índice 5 com os da coluna de índice 9. No final mostre a matriz.

matriz = []
matriz_aux = []
cont = 0

# para atribuir 100 valores para a matriz utilizei um contador
for l in range(10):
    lista = []
    for c in range(10):
        lista.append(cont)
        cont = cont + 1
    matriz.append(lista)

print("Matriz 10 por 10:")
for p in matriz:
    print(p)

# Trocar linha 2 por 8
# uso do fatiamento [inicio : fim] como não foi definido inicio e fim pega-se todas as colunas da linha 2 
matriz_aux = matriz[2][:]
for n in range(10):
    matriz[2][n] = matriz[8][n]
    matriz[8][n] = matriz_aux[n]

print("Matriz com linhas alteradas:")
for p in matriz:
    print(p)

# Trocar linha 5(2) co coluna 9(4): setar a ram para 5, setar a 5 para 9 setar a 9 para ram
#matriz_aux = matriz[5][:]

#for n in range(10):
#    matriz[5][n] = matriz[n][9]
#    matriz[n][9] = matriz_aux[n]

# também funciona com uma váriavel auxiliar
for n in range(10):
    aux = matriz[5][n]
    matriz[5][n] = matriz[n][9]
    matriz[n][9] = aux

print("Matriz com linha e coluna alterada:")
for p in matriz:
    print(p)