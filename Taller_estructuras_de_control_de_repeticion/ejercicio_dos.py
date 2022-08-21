for i in range(1, 101):
    if (i % 2 == 0) or (i % 7 == 0):
        continue
    print(i, end=(" "))
