# Crie um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
# utilizando as seguintes formulas (onde h corresponde à altura):
# • Homens: (72.7∗ h)−58
# • Mulheres: (62,1∗ h)−44,7

h = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo, escreva F ou M: ")

if sexo == "M":
    peso = (72*7*h)-58
    print("Seu peso ideal é", peso)

elif sexo == "F":
    peso = (62.1*h)-44.7
    print("Seu peso ideal é ", peso)

else:
    print("Sexo inválido")