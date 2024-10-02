'''Ler 2 duas estruturas (lista, tupla ou conjunto), denominada R de 5 elementos e S de 10 elementos, ambos de inteiros. Gere outra estrutura X que possua os elementos comuns a R e a S. Considere que na mesma estrutura não haverá números repetidos.
'''
r = []
s = []
cont = 0

for i in range(0,5):
    r.add(int(input(f"Informe um valor para a posição r[{i}]: ")))

for i in range(0,10):
    s.add(int(input(f"Informe um valor para a posição s[{i}]: ")))

x = r & s

print("S",s)
print("R",r)
print(x)