suma = 0
while True:
    x = float(input("Ingresa un número (negativo para terminar): "))
    if x < 0:
        break
    suma += x
print("Suma de positivos:", suma)
