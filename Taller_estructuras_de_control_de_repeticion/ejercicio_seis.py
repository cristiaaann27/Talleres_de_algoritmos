numero_uno = int(input(""))
numero_dos = int(input(""))

restas = 0
while True:
    numero_uno -= numero_dos
    restas += 1
    if ((numero_uno - numero_dos) < 0):
        break
print(f"Restas = {restas}, resto de la division = {numero_uno}")
