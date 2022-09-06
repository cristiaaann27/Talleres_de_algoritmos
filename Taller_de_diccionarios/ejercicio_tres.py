usuarios = {"iperurena": {"nombre": "Iñaki", "apellido": "Perurena", "password": "123123"}, "fmuguruza": {"nombre": "Fermín",
                                                                                                          "apellido": "Muguruza", "password": "654321"}, "aolaizola": {"nombre": "Aimar", "apellido": "Olaizola", "password": "123456"}}


def login(datos: dict):
    for _ in range(0, 3):
        usuario = input("Escriba su usuario: ")
        contrasena = input("Escriba su password: ")
        if usuario in datos and contrasena == datos[usuario]['password']:
            nombre = datos[usuario]['nombre']
            apellido = datos[usuario]['apellido']
            print(f"Login correcto, {nombre} {apellido}")
            break
        else:
            print("Login Incorrecto")
    return "Finalizado"


print(login(usuarios))
