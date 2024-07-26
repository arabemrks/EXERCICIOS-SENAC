matriz = [[1, 2, 11, 13],
          [4, 15, 16, 60],
          [7, 8, 19, 200],
          [20, 100, 5, 3]]

cont = 0

for linha in matriz:
    for valor in linha:
        if valor > 10:
            cont += 1

print(f"Numeros maiores que 10 na matriz: {cont}") 