'''Elabore um algoritmo que receba as 3 notas de um aluno e uma letra. Se a letra for “A”, 
deve-se chamar uma sub-rotina que deverá calcular a média aritmética das notas dos alunos; 
Se a letra for “P”, deverá calcular a média ponderada, com pesos 5, 3 e 2. A média calculada deverá 
ser devolvida ao programa principal para, então, ser mostrada.'''

def media_aritmetica(x, y, z):
    media = (x + y + z)/3
    return media

def media_ponderada(x, y, z):
    media = ((x * 5) + (y * 3) + (z * 2))/ 10
    return media

nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))
nota3 = float(input("Informe a nota 3: "))
sel_media = input("Informe A para a média Aritmética e P para média ponderada: ")

if(sel_media == "A" or sel_media == "a"):
    resultado = media_aritmetica(nota1, nota2, nota3)
    print(f"O valor da média Aritmética é: {resultado}")
elif(sel_media == "P" or sel_media == "p"):
    resultado = media_ponderada(nota1, nota2, nota3)
    print(f"O valor da média Ponderada é: {resultado}")
else:
    print("Valor Informado Inválido para a seleção da média!")

