# entrada
# parciales
nota_parcial_uno = float(input("Ingresa la nota de tu primer parcial: "))
nota_parcial_dos = float(input("Ingresa la nota de tu segundo parcial: "))
nota_parcial_tres = float(input("Ingresa la nota de tu tercer parcial: "))

nota_parcial_final = ((nota_parcial_uno + nota_parcial_dos + nota_parcial_tres)/3)*(55/100)
#examen
nota_examen = float(input("Ingresa la nota de tu examen: "))
nota_examen_final = nota_examen *(30/100)

#trabajo
nota_trabajo = float(input("Ingresa la nota de tu trabajo: "))
nota_trabajo_final = nota_trabajo*(15/100)

#nota final
nota_final = nota_parcial_final + nota_examen_final + nota_trabajo_final

# salida
print(f"La nota final de la materia de computacion es: {nota_final:.2f}")