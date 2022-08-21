n = int(input(""))
k = int(input(""))

while ((n < 0) or (k < 0) or (n < k)):
    n = int(input(""))
    k = int(input(""))

print(f"{n} vs {k}")
contador = 1
while n > k:
    n -= contador
    contador += 1
    print(f"{n} vs {k}")
