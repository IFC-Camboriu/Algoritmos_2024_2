'''Ler 2 vetores, R de 5 elementos e S de 10 elementos, ambos de inteiros.
 Gere um vetor X que possua os elementos comuns a R e a S. 
 Considere que no mesmo vetor não haverá números repetidos. '''

r = []
s = []
x = []

for i in range(0,5):
    r.append(int(input(f"Informe um valor para a posição r[{i}]: ")))

for i in range(0,10):
    s.append(int(input(f"Informe um valor para a posição s[{i}]: ")))

for i in range(0,5): # percorre r
    for j in range(0, 10): # percorre s
        if (r[i] == s[j]): # compara se o valor existe na outra estrutura
            x.append(r[i]) 

print(x)