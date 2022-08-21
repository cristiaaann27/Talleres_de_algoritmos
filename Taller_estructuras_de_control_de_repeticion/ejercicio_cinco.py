k = 1
sumatoria = (((k**2)+1)/k)
while sumatoria < 1000:
    print(f"{sumatoria:.6f}")
    sumatoria = (((k**2)+1)/k)
    k += 1
print(f"El numero necesario de k fue: {k-1}")
