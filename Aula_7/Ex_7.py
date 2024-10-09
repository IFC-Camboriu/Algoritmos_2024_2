'''Faça um algoritmo que percorre uma lista com o seguinte formato: [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]. Essa lista indica o número de faltas que cada time fez em cada jogo. Na lista acima, no jogo entre Brasil e Itália, o Brasil fez 10 faltas e a Itália fez 9. O programa deve imprimir na tela: 
o total de faltas do campeonato;
o time que fez mais faltas;
o time que fez menos faltas;
'''
lista_times = []
lista_faltas = []
total_faltas = []
indice_maior_numero_faltas = 1
indice_menor_numero_faltas = 1

jogos = [['Brasil', 'Italia', [10, 9]],
         ['Brasil', 'Espanha', [5, 7]], 
         ['Italia', 'Espanha', [7, 8]]]

# transformando em uma lista de times e outra lista de faltas
for l in range(len(jogos)):
    for c in range(len(jogos)-1):
        lista_times.append(jogos[l][c])
        lista_faltas.append(jogos[l][2][c])

print(lista_times)
print(lista_faltas)

# definindo o total de faltas
print(f"O total de faltas do campeonato é: {sum(lista_faltas)}")

for i in range(0, len(lista_times)):
    # se o time não está na lista adiciona o time e as faltas
    if(lista_times[i] not in total_faltas):
        total_faltas.append(lista_times[i])
        total_faltas.append(lista_faltas[i])
    else:
        # se o time está na lista encontra na lista total_faltas e soma as faltas
        for j in range(len(total_faltas)):
            if(total_faltas[j] == lista_times[i]):
                total_faltas[j + 1] = total_faltas[j + 1]  + lista_faltas[i]

print("Times e o total de faltas de cada time")
print(total_faltas)

for i in range(1, len(total_faltas), 2):
    # encontra o índice do maior e do menor número de faltas
    if(total_faltas[i] > total_faltas[indice_maior_numero_faltas]):
        indice_maior_numero_faltas = i
    if(total_faltas[i] < total_faltas[indice_menor_numero_faltas]):
        indice_menor_numero_faltas = i 

# após definir o indice do maior e do menor exibe o nome do time, por isso do -1
print(f"O time com menos faltas é: {total_faltas[indice_menor_numero_faltas-1]}")
print(f"O time com mais faltas é: {total_faltas[indice_maior_numero_faltas-1]}")