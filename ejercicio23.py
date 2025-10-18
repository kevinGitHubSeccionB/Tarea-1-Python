n = int(input("Ingresa un entero positivo n: "))
suma = 0
for i in range(2, n+1, 2):
    suma += i
print("Suma de pares desde 1 hasta", n, ":", suma)
