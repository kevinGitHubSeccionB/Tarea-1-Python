lim = int(input("Generar Fibonacci hasta (valor máximo): "))
a, b = 0, 1
while a <= lim:
    print(a)
    a, b = b, a + b
