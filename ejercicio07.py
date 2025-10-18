from datetime import datetime
year = int(input("Ingresa tu año de nacimiento: "))
actual = datetime.now().year
if 1900 < year < actual:
    print("Año de nacimiento válido")
else:
    print("Año inválido")
