# entrada
sueldo_base = float(input("Ingrese su sueldo base: "))
venta_uno = float(input("Ingrese el valor de la primera venta: "))
venta_dos = float(input("Ingrese el valor de la segunda venta: "))
venta_tres = float(input("Ingrese el valor de la tercera venta: "))

# caja negra
comisiones = (venta_uno + venta_dos + venta_tres)*(10/100)
sueldo_total = sueldo_base + comisiones

#salida
print(f"El valor de las comisiones es: ${comisiones:.2f}, y el sueldo total es: ${sueldo_total:.2f}" )


