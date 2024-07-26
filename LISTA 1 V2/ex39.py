# Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas
# no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.

valhora = float(input("Digite o valor da hora de trabalho: "))
numhora = float(input("Digite o Numero de horas trabalhadas: "))

cont = valhora * numhora
x = cont + (cont * 0.10)

print("O valor a ser pago ao funcionário é: ", x)