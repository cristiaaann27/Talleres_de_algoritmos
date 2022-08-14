categoria = int(input("Ingresa tu categoria: "))
sueldo = float(input("Ingresa tu sueldo: "))

# Categoria 1
if (categoria == 1):
    aumento = sueldo * (10/100)
    total = sueldo + aumento
    
# Categoria 2 
elif (categoria == 2):
    aumento = sueldo * (15/100)
    total = sueldo + aumento
 
# Categoria 3
elif (categoria == 3):
    aumento = sueldo * (20/100)
    total = sueldo + aumento
    
# Categoria 4
elif (categoria == 4):
    aumento = sueldo * (40/100)
    total = sueldo + aumento

# Categoria 5
elif (categoria == 5):
    aumento = sueldo * (60/100)
    total = sueldo + aumento
    
else:
    print("Categoria inexistente")
    
    
print(f"Tu nuevo sueldo es de: ${total}")