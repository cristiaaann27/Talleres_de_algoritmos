# entrada
dinero_ingresado = float(input("Ingrese la cantidad de dinero invertido: "))

# caja negra
valor_razon = dinero_ingresado * (2/100)
dinero_total = dinero_ingresado + valor_razon

# salida
print(f"El dinero ganado es: ${dinero_total:.2f}")