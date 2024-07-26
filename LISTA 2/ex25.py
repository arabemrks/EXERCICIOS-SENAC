# Crie uma mini calculadora mostre ao usuário um menu com 4 opções de operações matemáticas
# (as básicas, por exemplo). O usuário escolhe uma das opções e o seu programa então pede dois
# valores numéricos e realiza a operação, mostrando o resultado e finalizando o programa.

print("Escolha uma das opções e realize a operação")
print("1 - Soma, 2 - Subtração, 3 - Multiplicação e 4 - Divisão")

op = input("Digite a operação com o número correspondente de 1 a 4: ")

x = float(input("Digite um número: "))
y = float(input("Digite outro número: "))

if op == "1":
    soma = x + y
    print(f"A soma dos numeros é: {soma}")

elif op == "2":
    sub = x - y
    print(f"A subtração dos numeros é: {sub}")

elif op == "3":
    mult = x * y
    print(f"A multiplicação dos numeros é: {mult}")

elif op == "4":
    div = x / y
    print(f"A divisão dos numeros é: {div}")

else:
    print("Operação Inválida")