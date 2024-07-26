# Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim
# como a diferença existente entre ambos.

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

if num1 > num2:
    print(f"O primeiro número é maior que o segundo")
    dif = num1 - num2
    print(f"A diferença entre eles é {dif}")

elif num2 > num1:
    print(f"O Segundo número é maior que o primeiro")
    dif2 = num2 - num1
    print(f"A diferença entre eles é {dif2}")