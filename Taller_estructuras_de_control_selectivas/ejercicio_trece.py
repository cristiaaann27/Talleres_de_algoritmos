from datetime import date

today = date.today()

año_a = today.year
mes_a = today.month
dia_a = today.day

fecha_nacimiento = input("Ingresa tu fecha de nacimiento: ")
(año, mes, dia) = fecha_nacimiento.split("/")
año_n = int(año)
mes_n = int(mes)
dia_n = int(dia)

# edad
edad = 0
if (mes_a == mes_n):
    if (dia_a >= dia_n):
        edad = año_a - año_n
    else:
        edad = (año_a-año_n)-1
elif (mes_a > mes_n):
    edad = año_a - año_n
elif mes_a < mes_n:
    edad = (año_a-año_n)-1

# signo
signo = ""


if mes_n == 1:
    if dia_n >= 21:
        signo += "Acuario"
    else:
        signo += "Capricornio"

elif mes_n == 2:
    if dia_n >= 20:
        signo += "Piscis"
    else:
        signo += "Acuario"

elif mes_n == 3:
    if dia_n >= 21:
        signo += "Aries"
    else:
        signo += "Piscis"

elif mes_n == 4:
    if dia_n >= 21:
        signo += "Tauro"
    else:
        signo += "Aries"

elif mes_n == 5:
    if dia_n >= 22:
        signo += "Geminis"
    else:
        signo += "Tauro"

elif mes_n == 6:
    if dia_n >= 22:
        signo += "Cancer"
    else:
        signo += "Geminis"

elif mes_n == 7:
    if dia_n >= 23:
        signo += "Leo"
    else:
        signo += "Cancer"

elif mes_n == 8:
    if dia_n >= 24:
        signo += "Virgo"
    else:
        signo += "Leo"

elif mes_n == 9:
    if dia_n >= 23:
        signo += "Libra"
    else:
        signo += "Virgo"

elif mes_n == 10:
    if dia_n >= 23:
        signo += "Escorpion"
    else:
        signo += "Libra"
elif mes_n == 11:
    if dia_n >= 22:
        signo += "Sagitario"
    else:
        signo += "Escorpion"

elif mes_n == 12:
    if dia_n >= 22:
        signo += "Capricornio"
    else:
        signo += "Sagitario"


print(f"Tienes {edad} años")
print(f"Tu signo zodiacal es {signo}")
