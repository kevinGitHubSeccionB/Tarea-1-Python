n = int(input("Ingresa un número entero >= 2: "))
if n < 2:
    print("No es primo")
else:
    es_primo = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            es_primo = False
            break
        i += 1
    print("Primo" if es_primo else "No es primo")
