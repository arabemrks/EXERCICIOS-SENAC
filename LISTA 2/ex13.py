# Crie um programa que receba dois números e mostre o maior. Se por acaso, os dois números
# forem iguais, imprima a mensagem: Números iguais.

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

if num1 > num2:
    print(f"O primeiro número é maior que o segundo")

elif num2 > num1:
    print(f"O Segundo número é maior que o primeiro")

elif num1 == num2:
    print(f"Números iguais")