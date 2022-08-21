alcohol = 0
gasolina = 0
diesel = 0
while True:
    number = int(input(""))
    if number == 1:
        alcohol += 1
    elif number == 2:
        gasolina += 1
    elif number == 3:
        diesel += 1
    elif number == 4:
        break

print(
    f"MUITO OBRIGADO\nAlcool: {alcohol}\nGasolina: {gasolina}\nDiesel: {diesel}")
