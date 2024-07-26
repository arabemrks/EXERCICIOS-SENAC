matriz = []

for i in range(5):
    linha = []
    for num in range(5):
        if i == num:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)

for linha in matriz:
    print(linha)