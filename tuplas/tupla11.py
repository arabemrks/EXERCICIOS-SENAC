matriz = [[1, 2, 11, 13],
          [4, 15, 16, 60],
          [7, 8, 19, 200],
          [20, 100, 5, 3]]

maior_linha = 0
maior_coluna = 0
maior = matriz[0][0]

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if maior < matriz[i][j]:
            maior = matriz[i][j]
            maior_linha = i
            maior_coluna = j

print('Linha do maior numero: {}\nColuna do maior numero: {}'. format(maior_linha, maior_coluna))