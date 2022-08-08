#entrada
metros = float(input("Ingresa la medida en metros: ")) 

#caja negra
pulgadas = metros * 39.27
pies = pulgadas / 12

# salida
print(f"La conversion a pulgadas es: {pulgadas:.2f} in, y a pies es: {pies:.2f} ft.")