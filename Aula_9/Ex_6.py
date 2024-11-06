'''Faça uma função que inverte uma matriz 10 x 10 (linhas viram colunas e colunas viram linhas). '''

N = 3
def transpoe(matriz):
    aux_mat = []
    for l in range(N):
        lista = []
        for c in range(N):
            lista.append(matriz[c][l])
        aux_mat.append(lista)
#   return(aux_mat) 
    print(aux_mat)

mat = []

for l in range(N):
    aux = []
    for c in range(N):
        aux.append(int(input("Informe valores:")))
    mat.append(aux)

print(mat)

transpoe(mat)