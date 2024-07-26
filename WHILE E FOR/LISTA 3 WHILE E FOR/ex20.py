numeros = []

numeros.append(int(input("Digite um número: ")))
numeros.append(int(input("Digite um número: ")))
numeros.append(int(input("Digite um número: ")))
numeros.append(int(input("Digite um número: ")))
numeros.append(int(input("Digite um número: ")))

while sum(numeros) % 2 == 0:
    print("Par")
    break

else:
    print("Ímpar")