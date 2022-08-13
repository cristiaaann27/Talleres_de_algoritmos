# entrada
total_compra = float(input("Ingresa el monto total de la compra: "))

# caja negra
if total_compra > 5000000:
    inversion = total_compra * (55/100)
    prestamo_banco = total_compra * (30/100)
    credito = total_compra - (inversion + prestamo_banco)
    interes = credito * (20/100)
    total_pago = inversion + prestamo_banco + credito + interes

    print(
        f"La cantidad invertida de la empresa es: ${inversion} \nLa cantidad del credito es: ${credito} \nLos intereses a pagar por el credito son: ${interes} \nEs necesario el dinero prestado del banco, el cual es de: ${prestamo_banco} \nEl total a pagar es: ${total_pago}")
elif 0 < total_compra <= 5000000:
    inversion = total_compra * (70/100)
    credito = total_compra * (30/100)
    interes = credito * (20/100)
    total_pago = inversion + credito + interes
    print(
        f"La cantidad invertida de la empresa es: ${inversion} \nLa cantidad del credito es: ${credito} \nLos intereses a pagar por el credito son: ${interes} \nNo es necesario el dinero prestado del banco \nEl total a pagar es: ${total_pago}")
