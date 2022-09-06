def contar(lista: list):

    diccionario = {}
    for clave in lista:
        valor = lista.count(clave)
        diccionario.update({clave: valor})

    return diccionario


print(contar([12, 23, 5, 12, 92, 5, 12, 5, 29, 92, 64, 23]))
