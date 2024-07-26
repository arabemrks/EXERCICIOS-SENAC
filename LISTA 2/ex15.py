# Crie um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela
# a média destas notas. Uma nota valida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0,
# onde caso a nota não possua um valor válido, este fato deve será informado ao usuário e o
# programa termina.

num1 = int(input("Digite a primeira nota: "))
num2 = int(input("Digite a segunda nota: "))

if 0.0 <= num1 <= 10.0 and 0.0 <= num2 <= 10.0:
    med = (num1 + num2)/2
    print(f"A média é {med}")

else:
    print("Valor inválido")