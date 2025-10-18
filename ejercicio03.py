a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))
mayor = a
if b > mayor:
    mayor = b
if c > mayor:
    mayor = c
print("El mayor es:", mayor)
