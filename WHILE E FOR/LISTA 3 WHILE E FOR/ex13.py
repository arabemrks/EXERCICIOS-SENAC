numeros = []
n = int(input("Digite um numero: "))

cont = -1
while cont < n:
    cont = cont + 1
    numeros.append(cont)

numeros.sort(reverse=True)
print(numeros)
print("Fim do Programa")
