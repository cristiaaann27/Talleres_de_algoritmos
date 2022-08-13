temperatura = float(input("Ingresa la temperatura en grados Fahrenheit: "))

if (0 <= temperatura <= 10):
    deporte = "Marcha"

elif (10 < temperatura <= 32):
    deporte = "Esqui"

elif (32 < temperatura <= 70):
    deporte = "Golf"

elif (70 < temperatura <= 85):
    deporte = "Tenis"

elif (85 < temperatura <= 200):
    deporte = "Natacion"

else:
    deporte = "Las condiciones son extremas para practicar un deporte."

print(f"Tu deporte es: {deporte}")
