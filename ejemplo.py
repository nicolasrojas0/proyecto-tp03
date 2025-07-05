positivos = []
negativos = []

print("Ingresa 20 números:")

for i in range(1, 21):
    numero = float(input(f"Número {i}: "))
    if numero >= 0:
        positivos.append(numero)
    else:
        negativos.append(numero)

print("\nNúmeros positivos:")
print(positivos)

print("\nNúmeros negativos:")
print(negativos)
