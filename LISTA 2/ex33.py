# Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e
# a quantidade. O programa deve calcular o valor a ser pago por aquele lanche. Considere que a
# cada execução somente será calculado um pedido. O cardápio da lanchonete segue o padrão
# abaixo:
# Especificação   Código   Preço
# Hot Dog           100    12.00
# X-Salada          102    18.50
# X-BACON           103    25.50
# X-Burguer         104    17.00
# Suco de Laranja   105     9.50
# Refrigerante      106     6.00

cod100 = 12
cod102 = 18.50
cod103 = 25.50
cod104 = 17
cod105 = 9.50
cod106 = 6

cod = input("Digite o código do produto: ")
quant = int(input("Digite a quantidade escolhida: "))

if cod == "100":
    x = cod100 * quant
    print(f"Valor a ser pago é {x}")

elif cod == "102":
    x = cod102 * quant
    print(f"Valor a ser pago é {x}")

elif cod == "103":
    x = cod103 * quant
    print(f"Valor a ser pago é {x}")

elif cod == "104":
    x = cod104 * quant
    print(f"Valor a ser pago é {x}")

elif cod == "105":
    x = cod105 * quant
    print(f"Valor a ser pago é {x}")

elif cod == "106":
    x = cod106 * quant
    print(f"Valor a ser pago é {x}")

else:
    print("Código Inválido")