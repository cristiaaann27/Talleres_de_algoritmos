# entrada
lectura_anterior = int(input("Ingrese la lectura anterior de la luz: "))
lectura_actual = int(input("Ingrese la lectura actual de la luz: "))
precio_kv = float("Ingresa el precio del Kilovatio: ")

# caja negra
lectura = lectura_actual - lectura_anterior
monto_total = lectura * precio_kv

# salida
print(f"El precio total de la luz a pagar es: ${monto_total}")
