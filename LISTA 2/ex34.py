# Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e
# escreva o preço novo, e escreva uma mensagem em função do preço novo (de acordo com a
# segunda tabela).
# Preço antigo           Percentual de aumento
# até R$ 50                      5%
# entre R$ 50 e R$ 100          10%
# acima de R$ 100               15%

preco_antigo = float(input("Digite o preço antigo: "))

if preco_antigo < 50:
    x = preco_antigo + (preco_antigo * 0.05)
    print(f"O preço novo é {x}")

elif 50 <= preco_antigo < 100:
    x = preco_antigo + (preco_antigo * 0.10)
    print(f"O preço novo é {x}")

elif preco_antigo >= 100:
    x = preco_antigo + (preco_antigo * 0.15)
    print(f"O preço novo é {x}")