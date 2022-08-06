Algoritmo ejercicio_diecisiete
	Escribir "Ingresa la distancia entre los vehiculos en Km: "
	Leer distancia
	Escribir "Ingrese la velocidad del coche uno: "
	Leer velocidad_uno
	Escribir "Ingrese la velocidad del coche dos: "
	Leer velocidad_dos
	diferencia_de_velocidad <- abs(velocidad_uno-velocidad_dos)
	tiempo<- abs(distancia-diferencia_de_velocidad)
	tiempo <- tiempo * 60
	Escribir "El tiempo en el que alcanza el vehiculo al otro es de: ",tiempo, " minutos"
	
FinAlgoritmo
