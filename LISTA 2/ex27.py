'''
Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triangulo, se
forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:
• O comprimento de cada lado de um triangulo é menor do que a soma dos outros dois lados.
• Chama-se equilátero o triângulo que tem três lados iguais.
• Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
• Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
'''

lado1 = float(input("Digite o valor do primeiro lado: "))
lado2 = float(input("Digite o valor do segundo lado: "))
lado3 = float(input("Digite o valor do terceiro lado: "))

if lado1 < (lado2 + lado3) or lado2 < (lado1 + lado3) or lado3 < (lado2 + lado1):
    print("Valores verificados")
    if lado1 == lado2 == lado3:
        print("Equilátero")

    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("Isóceles")

    elif lado1 != lado2 != lado3:
        print("Escaleno")

else:
    print("Digite outros valores")