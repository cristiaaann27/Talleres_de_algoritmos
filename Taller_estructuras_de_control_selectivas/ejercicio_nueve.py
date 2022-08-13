nombre = input("Ingresa tu nombre: ")
valor_compra = float(input("Ingresa el monto de tu compra: "))

if valor_compra < 50000:
    total = valor_compra
    porcentaje_descuento = "No aplica"
    descuento = "No aplica"
elif 50000 <= valor_compra <= 100000:
    porcentaje_descuento = 5
    descuento = valor_compra * (5/100)
    total = valor_compra + descuento

elif 100000 < valor_compra <= 700000:
    porcentaje_descuento = 11
    descuento = valor_compra * (11/100)
    total = valor_compra + descuento

elif 700000 < valor_compra <= 1500000:
    porcentaje_descuento = 18
    descuento = valor_compra * (18/100)
    total = valor_compra + descuento

elif valor_compra > 1500000:
    porcentaje_descuento = 25
    descuento = valor_compra * (25/100)
    total = valor_compra + descuento

print(f"Señor: {nombre}\nEl monto de la compra es: ${valor_compra}\nEl total a pagar es: ${total}\nEl descuento recibido es de ${descuento}, gracias a un descuento del: {porcentaje_descuento}%")
