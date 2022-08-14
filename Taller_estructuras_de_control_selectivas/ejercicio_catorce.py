lectura_anterior = int(input("Ingresa la lectura anterior de luz: "))
lectura_actual = int(input("Ingresa la lectura actual de la luz: "))

diferencia = lectura_actual - lectura_anterior

if (0 < diferencia <= 100):
    total = diferencia * 4.600
elif (100 < diferencia <= 300):
    total = diferencia * 80.00
elif (300 < diferencia <= 500):
    total = diferencia * 100.00
elif (diferencia > 500):
    total = diferencia * 120.000
else:
    total = "Datos ingresados incorrectamente"

print(f"El total a pagar luz es: ${total}")