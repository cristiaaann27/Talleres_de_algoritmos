# entrada
sueldo_trabajador = int(input("Ingresa tu sueldo: "))

# caja negra
if sueldo_trabajador < 900000:
    nuevo_sueldo = sueldo_trabajador + (sueldo_trabajador * (15/100))
else:
    nuevo_sueldo = sueldo_trabajador + (sueldo_trabajador * (12/100))

# salida
print(f"Tu nuevo sueldo es de: ${nuevo_sueldo}")
