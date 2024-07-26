# Um brechó revende produtos usados, e fixa o preço de venda de cada produto conforme o valor
# de sua aquisição: Se o preço de aquisição de um produto é menor que R$ 50,00, ele deve ser
# vendido por um preço 45% maior, caso contrário o lucro será de 30%. Sabendo disso, Crie um
# algoritmo que leia o valor de aquisição de um produto e mostre o seu valor de venda.

aqs = float(input("Digite o valor de aquisição do produto: "))
x = aqs + (aqs * 0.45)
y = aqs + (aqs * 0.30)

if aqs < 50.00:
    print(f"O valor de venda é: {x}")

else:
    print(f"O valor de venda é: {y}")