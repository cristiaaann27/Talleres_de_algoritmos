p = int(input("Ingresa un numero: "))
q = int(input("Ingresa otro numero: "))

expresion = (p**3)+(q**4)-(2*(p**2))

if expresion > 680:
    print(f"{p} y {q} satisfacen la expresión")
else:
    print(f"{p} y {q} no Satisfacen la expresión")
