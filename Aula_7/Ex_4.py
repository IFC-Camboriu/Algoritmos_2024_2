#Faça um algoritmo que lê uma matriz M5X5 e crie 2 vetores(listas) SL (soma das linhas) 
# e SC (soma das colunas) com 5 posições cada. Adicionar aos vetores o resultado da soma
#  das linhas e das colunas da matriz, no final mostrar os dois vetores.

matriz  = []
SL = []
SC = []

# preenche a matriz com os valores
for i in range(5):
    matrizAux = []
    for j in range(5):
        matrizAux.append(int(input(f"Digite  o valor da linha {i + 1} coluna {j + 1}: ")))
    matriz.append(matrizAux)

#mostra os valores contidos na matriz
print("\nIMPRESSÃO DA MATRIZ.")  
for linha in matriz:
    for element in linha:
        print(element, end=" ")
    print()

#soma das linhas
'''for linha in matriz:
    soma = 0
    for element in linha:
        soma = soma + element
    SL.append(soma)'''

#soma as colunas
"""n = 0
for y in range(len(matriz)):
    soma = 0 
    for linha in matriz:
        soma = soma + linha[n]
    SC.append(soma)   
    n += 1"""

# soma das linhas e das colunas juntas
for n in range(5):
    SL.append(0)
    SC.append(0)
    for p in range(5):
        SL[n] = SL[n] + matriz[n][p]
        SC[n] = SC[n] + matriz[p][n]

print("\nSoma das Linha :",SL)
print("Soma das Coluna:",SC,"\n")