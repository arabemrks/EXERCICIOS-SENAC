# Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao
# vendedor. Para calcular a comissão, considere a tabela abaixo:
# Venda mensal Comissão
# Maior ou igual a R$100.000,00 R$700,00 + 16% das vendas
# Menor que R$100.000,00 e maior ou igual a R$80.000,00 R$650,00 +14% das vendas
# Menor que R$80.000,00 e maior ou igual a R$60.000,00 R$600,00 +14% das vendas
# Menor que R$60.000,00 e maior ou igual a R$40.000,00 R$550,00 +14% das vendas
# Menor que R$40.000,00 e maior ou igual a R$20.000,00 R$500,00 +14% das vendas
# Menor que R$20.000,00 R$400,00 +14% das venda

valor_venda = float(input("Digite o valor da venda: "))

if valor_venda >= 100.000:
    comissao = 700 + (valor_venda * 0.16)
    print(f"O valor da comissão é {comissao}")

elif 80.000 <= valor_venda < 100.000:
    comissao = 650 + (valor_venda * 0.14)
    print(f"O valor da comissão é {comissao}")

elif 60.000 <= valor_venda < 80.000:
    comissao = 600 + (valor_venda * 0.14)
    print(f"O valor da comissão é {comissao}")

elif 40.000 <= valor_venda < 60.000:
    comissao = 550 + (valor_venda * 0.14)
    print(f"O valor da comissão é {comissao}")

elif 20.000 <= valor_venda < 40.000:
    comissao = 500 + (valor_venda * 0.14)
    print(f"O valor da comissão é {comissao}")

elif valor_venda < 20.000:
    comissao = 400 + (valor_venda * 0.14)
    print(f"O valor da comissão é {comissao}")