# Crie um programa que leia 2 números inteiros e 1 real. Calcule e mostre: o produto do primeiro
# com a metade do segundo, a soma do triplo do primeiro com o terceiro. O terceiro número
# digitado ao cubo.

n1 = int(input("Digite um numero inteiro: "))
n2 = int(input("Digite outro numero inteiro: "))
n3 = float(input("Digite um numero real: "))

x = n1 * (n2/2)
y = (n1 * 3) + n3
z = n3 ** 3

print(f"O produto do primeiro número com a metade do segundo é: {x} \nA soma do triplo do primeiro com o terceiro número é: {y} \nO terceiro número ao cubo é: {z}")