from sys import float_repr_style


# entradas
precio_final = float(input("Ingresa el precio final pagado: "))
pvp = float(input("Ingresa el precio de venta al publico del producto: "))

# caja negra
descuento = (precio_final * 100) / pvp
porcentaje_descuento = 100 - descuento

# salida
print(f"El porcentaje de descuento de la compra es: {porcentaje_descuento}%")
