# entrada
valor_compra = float(input("ingrese el valor de la compra: "))
# caja negra
descuento = valor_compra*(15/100)
total_compra = valor_compra - descuento
# salida
print(f"El valor total de la compra es: ${total_compra:.2f}")