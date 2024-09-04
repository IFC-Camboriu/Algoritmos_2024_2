# A prefeitura de uma cidade fez uma pesquisa com 100 pessoas, coletando dados sobre o salário e o	número de filhos. A prefeitura deseja	 saber:	 
# A média do salário dessas pessoas
# A média do número de filhos
# O maior salário
# A percentagem de pessoas com salários até R$ 1500,00


soma_salario = 0
qtd_filhos = 0
maior_salario = 0
sal_ate_1500 = 0
TAM = 5

contador = 0

while contador < TAM:
    salario = float(input("Digite o salário: "))
    filhos = int(input("Digite o número de filhos: "))

    soma_salario += salario # soma de todos os salarios
   
    if salario > maior_salario:
        maior_salario = salario # identifica o maior salario

    if salario <= 1500:
        sal_ate_1500 += 1 # conta salarios menores que 1500
   
    qtd_filhos += filhos # total de filhos

    contador += 1 # controla o laço

print(f"A média de salário é {soma_salario/contador}")
print(f"A média de números de filhos é {qtd_filhos/contador}")
print(f"O maior salário é {maior_salario}")
print(f"A porcentagem de pessoas com renda até R$ 1.500 é {(sal_ate_1500/contador)*100}")
