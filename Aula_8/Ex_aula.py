#1
def maior(a, b):
    return max(a, b)

#2
def e_par(x):
    if x % 2 == 0:
        return True
    else:
        return False

#3
def area_quadrado(x):
    return x ** 2

#4
def area_triangulo(b, a):
    return (b*a)/2

x = 2
y = 5

print(maior(x,y))
print(e_par(6))
print(area_quadrado(6))
print(area_triangulo(6, 9))