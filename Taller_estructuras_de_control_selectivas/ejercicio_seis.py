a = int(input("Digite un numero: "))
b = int(input("Digite un numero: "))
c = int(input("Digite un numero: "))
d = int(input("Digite un numero: "))

redondeo_uno = c * 10 + d
if redondeo_uno >= 50:
    b += 1
redondeo_dos = (a*1000) + (b * 100)

print(f"El redondeo es: {redondeo_dos}")
