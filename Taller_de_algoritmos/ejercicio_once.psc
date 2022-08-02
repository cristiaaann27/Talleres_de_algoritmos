Algoritmo ejercicio_once
	Escribir 'Ingresa la nota del parciales'
	Leer nota_parcial_uno
	Leer nota_parcial_dos
	Leer nota_parcial_tres
	Escribir 'Ingresa la nota del examen'
	Leer nota_examen
	Escribir 'Ingresa nota del trabajo'
	Leer nota_trabajo
	nota_parcial_final <- ((nota_parcial_uno+nota_parcial_dos+nota_parcial_tres)/3)*(55/100)
	nota_examen_final <- (nota_examen)*(30/100)
	nota_trabajo_final <- (nota_trabajo)*(15/100)
	nota_final <- nota_parcial_final+nota_examen_final+nota_trabajo_final
	Escribir 'Nota final: ',nota_final
FinAlgoritmo
