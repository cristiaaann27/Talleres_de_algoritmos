total_encuestado = 0
consume = 0
no_consume = 0
aguardiente = 0
ron = 0
cerveza = 0
tequila = 0
whisky = 0
otro = 0
menor_de_edad = 0
mayor_de_edad = 0
mujer = 0
hombre = 0

caso_dos = 0
caso_tres = 0
caso_cuatro = 0
while True:
    total_encuestado += 1
    print("-------- Encuesta sobre consumo de licor --------- ")

    licor = input("¿Consume licor? (si o no): ").lower()
    if licor == "si":
        consume += 1

        licor_preferido = int(input(
            "Licor prefereido 1- Aguardiante, 2-Ron, 3-Cerveza, 4-Tequila,5-Whisky, 6-Otro: "))

        if licor_preferido == 1:
            aguardiente += 1
        elif licor_preferido == 2:
            ron += 1
        elif licor_preferido == 3:
            cerveza += 1
        elif licor_preferido == 4:
            tequila += 1
        elif licor_preferido == 5:
            whisky += 1
        elif licor_preferido == 6:
            otro += 1
        else:
            print("Respuesta invalida")
            break

        edad = int(input("Edad: "))
        if 0 < edad < 18:
            menor_de_edad += 1
        elif edad >= 18:
            mayor_de_edad += 1
        else:
            print("Respuesta invalida")
            break

        sexo = input("escribe si eres hombre o mujer: ").lower()
        if sexo == "hombre":
            hombre += 1
        elif sexo == "mujer":
            mujer += 1
        else:
            print("Respuesta invalida")
            break

        if sexo == "mujer" and edad < 18:
            caso_dos += 1

        if 20 <= edad <= 25 and sexo == "hombre" and licor_preferido != 1:
            caso_tres += 1

        if licor_preferido == 3:
            caso_cuatro += edad

    elif licor == "no":
        no_consume += 1

        edad = int(input("Edad: "))
        if 0 < edad < 18:
            menor_de_edad += 1
        elif edad >= 18:
            mayor_de_edad += 1
        else:
            print("Respuesta invalida")
            break

        sexo = input("escribe si eres hombre o mujer: ").lower()
        if sexo == "hombre":
            hombre += 1
        elif sexo == "mujer":
            mujer += 1
        else:
            print("Respuesta invalida")
            break

    else:
        print("Respuesta invalida")
        break

    finalizar = input("¿Quieres seguir con la encuesta? ").lower()
    if finalizar == "no":
        break


print(f"El total de personas encuestadas que consumen licor es: {consume}")
print(f"El total de mujeres menores de edad es: {caso_dos}")
print(
    f"El total de hombres que no consumen aguardiente y que tiene entre 20 y 25 años de edad es: {caso_tres}")
print(
    f"El promedio de edad de las personas que consumen cerveza es: {caso_cuatro//cerveza} años.")
print(
    f"El porcentaje de personas que consumen whisky en relación con el total encuestadoes: {((whisky/total_encuestado)*100):.2f} %")
