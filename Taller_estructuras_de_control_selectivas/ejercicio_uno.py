# entrada
inversion = int(input("Ingresa la cantidad de dinero invertido: "))
valor_interes = int(input("Ingresa el interes que ofrece el banco: "))/100

# caja negra
interes = inversion * valor_interes

if interes > 100000:
    total = inversion + interes
    # salida
    print(f"En su cuenta hay ${total}")
else:
    print(f"El valor de interes es: {interes}")
