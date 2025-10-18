suma = 0
count = 0
print("Ingresa números (negativo para terminar):")
while True:
    x = float(input())
    if x < 0:
        break
    suma += x
    count += 1
if count == 0:
    print("No se ingresaron números válidos")
else:
    print("Media:", suma / count)
