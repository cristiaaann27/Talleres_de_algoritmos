# entrada
galones = float(input("Ingresa los galones que adquirio el cliente: "))

#caja negra
litros = galones * 3.785
precio_gasolina = litros * 50000

# salida
print(f"El precio de {galones} galones de gasolina es: ${round(precio_gasolina)}")