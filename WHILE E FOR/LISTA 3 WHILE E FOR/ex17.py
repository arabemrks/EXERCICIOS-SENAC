numeros = []
n = int(input("Digite um numero: "))

soma = 0
cont = -1
while cont < n:
    cont = cont + 1
    numeros.append(cont)
    soma = soma + cont


print(soma)

print("Fim do Programa")