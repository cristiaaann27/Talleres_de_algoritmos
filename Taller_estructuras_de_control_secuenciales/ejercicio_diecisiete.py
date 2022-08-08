# entrada
presupuesto_anual = float(input("Ingresa el presupuesto del hospital: "))

# caja negra
ginecologia = presupuesto_anual * (40/100)
traumatologia = presupuesto_anual * (30/100)
pediatria = presupuesto_anual * (30/100)

# salida
print(f"El area de ginecologia recibe ${ginecologia:.3f}, el area de traumatologia recibe ${traumatologia:.3f}, y el area de pedriatria recibe ${pediatria:.3f}")