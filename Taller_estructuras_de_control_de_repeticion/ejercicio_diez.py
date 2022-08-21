n = int(input("Ingresa la cantidad de estudiantes a medir: "))

contador = 1
estatura_mayor = 0

while contador <= n:
    contador += 1
    estatura = int(input("Ingresa la estatura del estudiante en cm: "))

    if estatura > estatura_mayor:
        estatura_mayor = estatura

print(f"La estatura mas alta es de: {estatura_mayor} cm")
