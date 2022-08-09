# entrada
naranjas = int(input("Ingresa la cantidad de naranjas compradas: "))
docena = int(input("Ingresa el valor de la docena de naranjas compradas: "))
ganancia = int(input("Ingresa la ganancia de las naranjas compradas: "))

# caja negra
cantidad_docena = naranjas / 12
valor_total = cantidad_docena * docena
porcentaje_ganancias = (ganancia / valor_total) * 100

# salida
print(f"El porcentaje de ganancias es: {porcentaje_ganancias}%")
