matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
soma = 0
 
for i in matriz:
    for j in matriz:
        soma =  matriz[0][0] + matriz[1][1] + matriz[2][2]
 
print('A soma é: {}'. format(soma))