from math import sqrt
# Entradas
a = float(input("Digite el lado a: "))
b = float(input("Digite el lado b: "))
c = float(input("Digite el lado c: "))

# Caja negra
s = (a + b + c)/2
area = sqrt(s*(s-a)*(s-b)*(s-c))

#Salida 
print(f"El area es: {str(area)}")