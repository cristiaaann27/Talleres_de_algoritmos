# entrada
a = int(input("Ingresa numero a: "))
b = int(input("Ingresa numero b: "))
c = int(input("Ingresa numero c: "))
d = int(input("Ingresa numero d: "))

# caja negra
if d == 0:
    resultado = (a-c)**2
elif d > 0:
    resultado = (a-b)**3

print(f"El resultado de las la expresion es: {resultado}")
