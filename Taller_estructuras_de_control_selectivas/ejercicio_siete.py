kilometros = float(input("Ingrese los kilometros recorridos: "))

if 0 < kilometros <= 300:
    cobro = 50000
    print(f"El total a pagar es ${cobro} COP")
elif kilometros > 300:
    if kilometros <= 1000:
        cobro = 70000
        kilometros_adicionales = kilometros - 300
        cobro_adicional = kilometros_adicionales * 30000
        total = cobro + cobro_adicional
        print(f"El total a pagar es ${total} COP")
    elif kilometros > 1000:
        cobro = 150000
        kilometros_adicionales = kilometros - 300
        cobro_adicional = kilometros_adicionales * 9000
        total = cobro + cobro_adicional
        print(f"El total a pagar es ${total} COP")
