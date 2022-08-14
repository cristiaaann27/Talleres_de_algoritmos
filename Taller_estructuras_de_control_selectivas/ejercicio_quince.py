nivel_hemoglobina = float(input("Ingresa tu nivel de hemoglobina: "))
edad = int(input("Ingresa tu edad en meses: "))
sexo = int(input("si eres hombre ingresa 1, si eres mujer ingresa 0: "))

if (0<edad<=1):
    rango_menor = 13
elif (1<edad<=6):
    rango_menor = 10
elif (6<edad<=12):
    rango_menor = 11
elif (12<edad<=60):
    rango_menor = 11.5
elif (60<edad<=120):
    rango_menor = 12.6
elif (120<edad<=180):
    rango_menor = 13
elif (sexo == 0 and edad > 180):
    rango_menor = 12
elif (sexo == 1 and edad > 180):
    rango_menor = 14
    
if nivel_hemoglobina < rango_menor:
    print("Positivo para anemia")
else:
    print("Negativo para hemoglobina")
    
print(f"Nivel minimo de hemoglobina: {rango_menor}")