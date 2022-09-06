def recorrer(diccionario: dict):

    lista = []
    for valor in diccionario:
        if not diccionario[valor] in lista:
            lista.append(diccionario[valor])
    return lista


print(recorrer({'Mikel': 3, 'Ane': 8, 'Amaia': 12,
      'Unai': 5, 'Jon': 8, 'Ainhoa': 7, 'Maite': 5}))
