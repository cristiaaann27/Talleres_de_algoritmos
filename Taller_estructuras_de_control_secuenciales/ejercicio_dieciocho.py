# entrada
capital = float(input("Ingresa el valor del prestamo: "))
razon = (float(input("Ingresa el valor del interes: ")))/100

# caja negra
interes = (capital * 4 * razon)/100

# salida
print(f"El cobro anual es de: {interes}%")
