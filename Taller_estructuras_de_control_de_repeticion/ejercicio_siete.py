while True:
    juego = input("")
    (x, m) = juego.split(" ")
    x = int(x)
    m = int(m)
    if x == 0 and m == 0:
        break
    elif x == 1 or x == 2 or x == 3:
        m *= x
        print(m)
