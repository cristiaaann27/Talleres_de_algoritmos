# Entradas
salario_mensual = float(input("Digite su salario bruto mensual: "))
ventas_departamento_uno = int(
    input("Ingrese las ventas totales del departamento uno: "))
ventas_departamento_dos = int(
    input("Ingrese las ventas totales del departamento dos: "))
ventas_departamento_tres = int(
    input("Ingrese las ventas totales del departamento tres: "))

# Caja negra
total_ventas = (ventas_departamento_uno +
                ventas_departamento_dos + ventas_departamento_tres)
porcentaje_ventas = 33/100
porcentaje_aumento = salario_mensual * (20/100)

if ((ventas_departamento_uno/total_ventas) > (porcentaje_ventas)):
    sueldo_final_uno = salario_mensual + porcentaje_aumento
    print(f"Los vendedores del departamento uno ganan: ${sueldo_final_uno}")
else:
    print(f"Los vendedores del departamento uno ganan: ${salario_mensual}")


if ((ventas_departamento_dos/total_ventas) > (porcentaje_ventas)):
    sueldo_final_dos = salario_mensual + porcentaje_aumento
    print(f"Los vendedores del departamento dos ganan: ${sueldo_final_dos}")
else:
    print(f"Los vendedores del departamento dos ganan: ${salario_mensual}")


if ((ventas_departamento_tres/total_ventas) > (porcentaje_ventas)):
    sueldo_final_tres = salario_mensual + porcentaje_aumento
    print(f"Los vendedores del departamento tres ganan: ${sueldo_final_tres}")
else:
    print(f"Los vendedores del departamento tres ganan: ${salario_mensual}")
