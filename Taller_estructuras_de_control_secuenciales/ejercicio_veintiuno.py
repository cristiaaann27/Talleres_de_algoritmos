# entrada
precio_contado = int(input("Ingresa el costo del computador al contado: "))
valor_cuota = int(input("Ingresa el costo la cuota mensual: "))

# caja negra
total_cuota = 12 * valor_cuota
porcentaje_cuota = ((total_cuota * 100) / precio_contado)/100

# salida
print(f"El porcentaje es: {porcentaje_cuota:.2f}%")
