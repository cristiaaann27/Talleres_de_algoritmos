# entrada
nombre = input("Ingresa tu nombre: ")
horas_trabajadas = int(input("Ingresa el numero de horas trabajadas: "))
valor_hora = float(input("Ingresa el valor de una hora normal: "))
horas_extra = int(input("Ingresa el numero de horas extra trabajadas: "))

# caja negra
valor_hora_extra = valor_hora + (valor_hora * (25/100))
valor_sueldo = (valor_hora*horas_trabajadas)+(valor_hora_extra * horas_extra)
deducciones = valor_sueldo*(14/100)
asignaciones = 250000+180000+173000
sueldo_neto = valor_sueldo - deducciones + asignaciones

# salida
print(
    f"El valor de las asignaciones es: ${asignaciones}, el valor de las deducciones es: ${deducciones:.2f} y el sueldo neto de {nombre} para diciembre es: ${sueldo_neto}")
