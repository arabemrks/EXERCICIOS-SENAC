# Crie um programa que leia um número inteiro e, caso ele seja positivo, calcule e mostre:
# • O número digitado ao quadrado;
# • A raiz quadrada do número digitado;

import math

num = int(input("Digite um número: "))

if num > 0:
    raiz = math.sqrt(num)
    quad = num ** 2
    print(f"O número ao quadrado é: {quad}\nA raiz quadrada é: {raiz}")

else:
    print("O número é inválido")