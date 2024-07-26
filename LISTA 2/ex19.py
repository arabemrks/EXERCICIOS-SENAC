# Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma
# de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se
# o número lido não for maior do que zero, o programa termina com a mensagem “Número
# inválido”

num = int(input("Digite um número: "))

if num > 0:
    str(num)
    soma = 0
    print(f"A soma dos algarismos é: {soma}")

else:
    print("Número Inválido")