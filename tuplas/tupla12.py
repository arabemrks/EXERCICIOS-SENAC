m = [[1,120, -3],
     [4, 5, 250],
     [7 , 0, 9 ]]

maior_linha = 0
maior_coluna = 0
maior = m[0][0]

menor_linha = 0
menor_coluna = 0
menor = m[0][0]

for i in range(len(m)):
    for j in range(len(m)):        
        if maior < m[i][j]:
            maior = m[i][j]
            maior_linha = i
            maior_coluna = j

for i in range(len(m)):
    for j in range(len(m)):        
        if menor > m[i][j]:
            menor = m[i][j]
            menor_linha = i
            menor_coluna = j

print('Linha do maior: {}\nColuna do maior: {}'.format(maior_linha, maior_coluna))
print('Linha do menor: {}\nColuna do menor: {}'.format(menor_linha, menor_coluna))