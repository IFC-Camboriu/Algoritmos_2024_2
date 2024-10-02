'''Faça um programa que preencha duas estruturas (lista, tupla ou conjunto), X e Y, com dez números inteiros cada. Calcule e mostre os seguintes o seguinte resultado:
A diferença entre X e Y, por exemplo:'''

x = set()
y = set()

for i in range(0,5):
    x.add(int(input(f"Informe um valor para a posição x[{i}]: ")))

for i in range(0,5):
    y.add(int(input(f"Informe um valor para a posição y[{i}]: ")))

dif = x - y
print("X",x)
print("Y",y)
print(f"Os valores da diferença são:{dif}")