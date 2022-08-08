# entradas
cantidad_billetes_cincuenta_mil = int(input("Ingresa la cantidad de billetes de $50000: "))*50000

cantidad_billetes_veinte_mil = int(input("Ingresa la cantidad de billetes de $20000: "))*20000

cantidad_billetes_diez_mil = int(input("Ingresa la cantidad de billetes de $10000: "))*10000

cantidad_billetes_cinco_mil = int(input("Ingresa la cantidad de billetes de $5000: "))*5000

cantidad_billetes_dos_mil = int(input("Ingresa la cantidad de billetes de $2000: "))*2000

cantidad_billetes_mil = int(input("Ingresa la cantidad de billetes de $1000: "))*1000

cantidad_billetes_quinientos = int(input("Ingresa la cantidad de billetes de $500: "))*500

cantidad_billetes_cien = int(input("Ingresa la cantidad de billetes de $100: "))*100

#caja negra 
dinero_total = cantidad_billetes_cincuenta_mil + cantidad_billetes_veinte_mil + cantidad_billetes_diez_mil + cantidad_billetes_cinco_mil + cantidad_billetes_dos_mil + cantidad_billetes_mil + cantidad_billetes_quinientos + cantidad_billetes_cien

# salida
print(f"El dinero total es: ${dinero_total}")