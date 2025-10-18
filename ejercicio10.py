precio = float(input("Precio del artículo: "))
desc = float(input("Porcentaje de descuento (ej: 20 para 20%): "))
if desc < 0 or desc > 100 or precio < 0:
    print("Entrada inválida")
else:
    final = precio * (1 - desc/100)
    print("Precio después del descuento:", round(final, 2))
