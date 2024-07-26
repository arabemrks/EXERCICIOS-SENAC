# Receba 3 números inteiros na entrada e imprima: crescente, se eles forem dados em ordem
# crescente. Caso contrário, imprima não está em ordem crescente.

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
num3 = int(input("Digite outro número inteiro: "))

if num1 < num2 < num3:
    print(f"Crescente")

else:
    print(f"Não está em ordem crescente")