Algoritmo ejercicio_nueve
	Escribir "Ingresa el sueldo base: "
	Leer sueldo_base
	Escribir "Ingresa la primera venta: "
	Leer primera_venta
	Escribir "Ingresa la segunda venta: "
	Leer segunda_venta
	Escribir "Ingresa la tercera venta: "
	Leer tercera_venta
	comision<-(primera_venta+segunda_venta+tercera_venta)*(10/100)
	sueldo_total <- sueldo_base + comision
	Escribir "El valor de las comisiones es: $",comision," y el sueldo total es: $",sueldo_total
	
	
FinAlgoritmo
