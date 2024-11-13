'''Crie uma sub-rotina que receba como parâmetro um vetor V[25] de números inteiros e substitua todos os valores negativos de A por 0. O vetor deverá ser mostrado no programa principal'''

def negativos(v):
    for y in range(len(v)):
       if (v[y] < 0):
            v[y] = 0

N = 10
v = []
for x in range(N):
    v.append(int(input("informe um valor: ")))

print(f"V:{v}")

negativos(v)

print (f"V:{v}")

a =[1, -2, 3, -5]

negativos(a)

print(f"A:{a}")