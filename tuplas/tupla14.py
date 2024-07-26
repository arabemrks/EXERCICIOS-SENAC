a = [[1, 13, 3], [4, 45, 67], [7, 80, 9]]
b = [[100, 8, 7], [6, 5, 4], [3, 25, 10]]
matriz_soma = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
 
for i in range(3):
    for j in range(3):
        matriz_soma[i][j] = a[i][j] + b[i][j]
 
print("\nMatriz Soma de A e B:")
for linha in matriz_soma:
    print(linha)