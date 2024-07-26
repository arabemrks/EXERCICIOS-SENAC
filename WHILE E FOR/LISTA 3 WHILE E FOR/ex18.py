numeros = []

cont = 0
while cont < 2:
    n = int(input("Digite um numero: "))
    cont = cont + 1
    numeros.append(n)


print(F"O maior número digitado é: {max(numeros)}")

print("Fim do Programa")