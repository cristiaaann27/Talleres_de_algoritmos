def proceso(nota_minima):
    diccionario = {}
    aprobado = []
    suspendido = []
    suma = 0

    for i in range(1, 11):
        nombre = input("Ingresa el nombre: ")
        nota = float(input("Ingresa la nota: "))
        diccionario.update({i: {"nombre": nombre, "nota": nota}})
        if nota < nota_minima:
            suspendido.append(nombre)
        else:
            aprobado.append(nombre)
        suma += nota
    promedio = suma / 10
    return diccionario, aprobado, suspendido, promedio


def imprimir(datos):
    (dictionary, lista_aprobado, lista_suspendido, prom) = datos
    print(dictionary)
    print(f"La lista de aprobado es: {lista_aprobado}")
    print(f"La lista de suspendido es: {lista_suspendido}")
    print(f"El promedio es: {prom}")


nota_minima_requierida = float(input("Ingresa la nota minima: "))

imprimir(proceso(nota_minima_requierida))
