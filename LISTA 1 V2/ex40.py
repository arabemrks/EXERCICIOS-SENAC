# Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que
# esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de
# imposto sobre o salário-base.

base = float(input("Digite o valor do seu salário base: "))

cont = base + (base * 0.05)
cont2 = cont - (base * 0.07)

print("O valor a ser pago ao funcionário é: ", cont2)