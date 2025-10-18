n = int(input("Ingresa un número entero (>0): "))
if n <= 0:
    print("Número inválido")
else:
    divisores = []
    for i in range(1, int(abs(n)**0.5) + 1):
        if n % i == 0:
            divisores.append(i)
            if i != n // i:
                divisores.append(n // i)
    divisores.sort()
    print("Divisores de", n, ":", divisores)
