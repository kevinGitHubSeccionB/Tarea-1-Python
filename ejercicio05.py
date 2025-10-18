ch = input("Ingresa una letra: ").strip().lower()
if len(ch) != 1 or not ch.isalpha():
    print("Entrada no válida")
else:
    if ch in "aeiou":
        print("Vocal")
    else:
        print("Consonante")
