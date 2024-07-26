n = 3
m = 3

matriz = []

for linha in range(n):
    lin = []
    for col in range(m):
        lin.append(input("Digite um valor: "))
    matriz.append(lin)

for i in matriz:
    print(i)