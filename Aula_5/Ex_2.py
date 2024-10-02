'''Ler uma estrutura (lista, tupla ou conjunto), R de 5 elementos, inteiros, contendo o resultado da LOTO. A seguir ler outra estrutura (lista, tupla ou conjunto), A de 10 elementos inteiros contendo uma aposta. A seguir imprima quantos pontos fez o apostador.
'''
r = set()
a = set()
cont = 0

for i in range(0,5):
    r.add(int(input(f"Informe um valor para a posição r[{i}]: ")))

for i in range(0,10):
    a.add(int(input(f"Informe um valor para a posição s[{i}]: ")))

x = r & a

print("A",a)
print("R",r)
print(f" O número de pontos é: {len(x)}")