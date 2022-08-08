# entradas
horas_trabajadas = int(input("Ingresa las horas trabajadas: "))
precio_hora = float(input("Ingresa el valor de la hora: "))

#caja negra
sueldo_base = horas_trabajadas * precio_hora
sueldo_neto = sueldo_base - (sueldo_base*(20/100))

# salida
print(f"El sueldo neto es: ${sueldo_neto}")