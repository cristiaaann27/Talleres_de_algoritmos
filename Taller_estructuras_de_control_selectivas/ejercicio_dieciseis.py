from math import sqrt
a = int(input("Ingresa el valor de a: "))
b = int(input("Ingresa el valor de b: "))
c = int(input("Ingresa el valor de c: "))

discriminante = ((b**2)-4*a*c)

if discriminante == 0:
    solucion = (-b/(2*a))
    print(f"La solucion es: {solucion}")
elif discriminante > 0:
    solucion_positiva = (-b+sqrt(discriminante))/(2*a)
    solucion_negativa = (-b-sqrt(discriminante))/(2*a)
    print(f"La solucion positiva es: {solucion_positiva} y la solucion negativa es: {solucion_negativa}")
else:
    print("No tiene solucion en los reales")