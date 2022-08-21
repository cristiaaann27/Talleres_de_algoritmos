n = int(input("Ingrese el numero de estudiantes: "))

contador = 1

nombre_puntaje_maximo = ""
nombre_puntaje_minimo = ""

puntaje_maximo = 0
puntaje_minimo = 10000000

inferiores_promedio = 0
superiores_promedio = 0
suma = 0

lista = []

while contador <= n:
    contador += 1
    nombre = input("Ingresa el nombre del estudiante: ")
    puntaje = int(input("Ingresa la calificacion: "))
    lista.append(puntaje)
    suma += puntaje

    if puntaje > puntaje_maximo:
        puntaje_maximo = puntaje
        nombre_puntaje_maximo = nombre
    elif puntaje < puntaje_minimo:
        puntaje_minimo = puntaje
        nombre_puntaje_minimo = nombre


promedio = suma/n

for i in lista:
    if i < promedio:
        inferiores_promedio += 1
    elif i > promedio:
        superiores_promedio += 1

porcentaje_inferiores = (inferiores_promedio / n) * 100
porcentaje_superiores = (superiores_promedio / n) * 100

print(
    f"El puntaje maximo es de: {nombre_puntaje_maximo} con un puntaje de {puntaje_maximo}")
print(
    f"El puntaje minimo es de: {nombre_puntaje_minimo} con un puntaje de {puntaje_minimo}")
print(f"El promedio de puntajes es: {promedio:.2f}")
print(
    f"El porcentaje de estudiantes con puntajes inferiores al promedio es: {porcentaje_inferiores:.2f}%")
print(
    f"El porcentaje de estudiantes con puntajes superiores al promedio es: {porcentaje_superiores:.2f}%")
