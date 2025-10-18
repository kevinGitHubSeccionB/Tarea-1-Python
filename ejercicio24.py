n = int(input("Ingresa un entero >=0: "))
if n < 0:
    print("No definido para negativos")
else:
    fact = 1
    for i in range(2, n+1):
        fact *= i
    print(f"{n}! =", fact)
