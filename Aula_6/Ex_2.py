'''Faça um algoritmo que lê uma matriz M5x5. A matriz deve ser preenchida através das colunas, por exemplo, se for digitado:
1,2,3,4,5,6,7,8,9,10,... 
Após mostre a matriz resultante.
'''

matriz =[[0, 0, 0], [0, 0, 0],[0, 0, 0] ]

c = 0
l = 0
# alteramos a lógica da linha(l) e coluna(c)
while c < len(matriz):
    l = 0 # necessário iniciar em 0 a cada nova linha que iniciamos
    while l < len(matriz):
        matriz[l][c] = int(input(f"Informe matriz[{l}][{c}]: "))
        l = l + 1
    c = c + 1

# mostrando a matriz(outra forma)
c = 0
l = 0   
while l < len(matriz):
    c = 0
    while c < len(matriz[l]):
        print(matriz[l][c], end=' ')
        c +=1
    print()
    l += 1
