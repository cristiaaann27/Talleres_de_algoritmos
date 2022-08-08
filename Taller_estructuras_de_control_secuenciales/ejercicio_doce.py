# Notas Matematicas
def matematicas(): 
    examen_math = float(input("Ingresa la nota de tu examen de matematicas: "))
    promedio_examen_math = (examen_math*(90/100))
    tarea_uno_math = float(input("Ingresa la nota de la tarea uno de matematicas: "))
    tarea_dos_math = float(input("Ingresa la nota de la tarea dos de matematicas: "))
    tarea_tres_math = float(input("Ingresa la nota de la tarea tres de matematicas: "))
    promedio_tareas_math = ((tarea_uno_math+tarea_dos_math+tarea_tres_math)/3)*(10/100)
    nota_final_math = promedio_examen_math + promedio_tareas_math
    return nota_final_math
# Notas Fisica
def fisica():   
    examen_fisica = float(input("Ingresa la nota de tu examen de fisica: "))
    promedio_examen_fisica = (examen_fisica*(80/100))
    tarea_uno_fisica = float(input("Ingresa la nota de la tarea uno de fisica: "))
    tarea_dos_fisica = float(input("Ingresa la nota de la tarea dos de fisica: "))
    promedio_tareas_fisica = ((tarea_uno_fisica+tarea_dos_fisica)/2)*(20/100)
    nota_final_fisica = promedio_examen_fisica + promedio_tareas_fisica
    return nota_final_fisica

# Notas Quimica
def quimica():
    examen_quimica = float(input("Ingresa la nota de tu examen de quimica: "))
    promedio_examen_quimica = (examen_quimica*(85/100))
    tarea_uno_quimica = float(input("Ingresa la nota de la tarea uno de quimica: "))
    tarea_dos_quimica = float(input("Ingresa la nota de la tarea dos de quimica: "))
    tarea_tres_quimica = float(input("Ingresa la nota de la tarea tres de quimica: "))
    promedio_tareas_quimica = ((tarea_uno_quimica+tarea_dos_quimica+tarea_tres_quimica)/3)*(15/100)
    nota_final_quimica = promedio_examen_quimica + promedio_tareas_quimica
    return nota_final_quimica

nota_final_math = matematicas()
nota_final_fisica = fisica()
nota_final_quimica = quimica()
promedio_semestre =(nota_final_math+nota_final_fisica+nota_final_quimica)/3
print(f"Matematicas: {nota_final_math}, Fisica: {nota_final_fisica}, Quimica: {nota_final_quimica}, y el promedio es: {promedio_semestre}")