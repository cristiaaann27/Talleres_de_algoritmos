 # de chelines austriacos a pesetas
def cambio_uno():
     pesetas = 956.871/100
     ingreso_chelines = float(input("Ingresa la cantidad de chelines austriacos: "))
     cambio = ingreso_chelines * pesetas
     print(f"El cambio de ${ingreso_chelines} chelines austriacos a pesetas, es: ${cambio:.3f}")
     

# de dracmas griegos a francos franceses
def cambio_dos():
    pesetas = 88.607/100
    ingreso_dracmas = float(input("Ingresa la cantidad de dracmas griegos: "))
    cambio_pesetas = pesetas * ingreso_dracmas
    cambio_francos = cambio_pesetas / 20.110
    print(f"El cambio de ${ingreso_dracmas} dracmas griegos a francos franceses es: ${cambio_francos:.3f}")


def cambio_tres():
    ingreso_pesetas = float(input("Ingresa la cantidad de pesetas: "))
    cambio_dolar = ingreso_pesetas / 122.499
    lira = 100/9.289
    cambio_lira = ingreso_pesetas * lira
    print(f"El cambio de ${ingreso_pesetas} pesetas a dolares es: ${cambio_dolar:.3f}, y a liras italianas es: ${cambio_lira:.3f}")

cambio_uno()
cambio_dos()
cambio_tres()
