# . Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
# • o total a pagar com desconto de 10%;
# • o valor de cada parcela, no parcelamento de 3× sem juros;
# • a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
# • a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)

valor = float(input("Digite o valor da venda: "))

porc = (valor * 10)/100
pagvista = valor - porc
parcela = valor/3

comissao_avista = pagvista * 0.05
comissao_aprazo = valor * 0.05

print(f"Compra com desconto: {pagvista}\n Parcelas: {parcela}\n Comissão a vista: {comissao_avista}\n Comissão a prazo: {comissao_aprazo}")