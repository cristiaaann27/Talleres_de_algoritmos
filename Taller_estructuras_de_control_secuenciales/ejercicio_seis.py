# entrada 
hombres = int(input("Ingrese la cantidad de hombres en el salon: "))
mujeres = int(input("Ingrese la cantidad de mujeres en el salon: "))
# caja negra
total_alumnos = (hombres + mujeres)/100
porcentaje_hombres = hombres / total_alumnos
porcentaje_mujeres = mujeres / total_alumnos
print(f"El porcentaje de hombres es: {round(porcentaje_hombres)}%, y el porcentaje de las mujeres es: {round(porcentaje_mujeres)}%")

