# Crie um programa de uma calculadora simples com as 4 operações básicas, apresente o menu
# de opções abaixo, leia dois números reais. Em seguida mostre o resultado da operação entre os
# dois números recebidos. Escreva uma mensagem de erro se a opção for inválida.
# Escolha a opção:
# 1- Soma de 2 números.
# 2- Diferença entre 2 números (maior pelo menor).
# 3- Produto entre 2 números.
# 4- Divisão entre 2 números (o denominador não pode ser zero).

print("Escolha uma das opções e realize a operação")
print("1 - Soma de 2 números\n2 - Diferença entre 2 números\n3 - Produto entre 2 números\n4 - Divisão entre 2 números")

op = input("Digite a operação com o número correspondente de 1 a 4: ")

x = float(input("Digite um número: "))
y = float(input("Digite outro número: "))

if op == "1":
    soma = x + y
    print(f"A soma dos numeros é: {soma}")

elif op == "2":
    sub = x - y
    print(f"A diferença dos numeros é: {sub}")

elif op == "3":
    mult = x * y
    print(f"O produto dos numeros é: {mult}")

elif op == "4" and y != 0:
    div = x / y
    print(f"A Divisão dos numeros é: {div}")

else:
    print("Operação Inválida")