pares = 0
impares = 0

while True:
    valor = int(input("Digite um número (0 para finalizar): "))
    
    if valor == 0:
        break

    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Você digitou {pares} números pares.")
print(f"Você digitou {impares} números ímpares.")
