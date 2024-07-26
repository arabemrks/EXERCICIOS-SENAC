# Em uma empresa paga-se R$ 40,50 a hora e recolhe-se para o imposto de renda 11% dos salários
# acima de R$ 2500,00. Dado o número de horas trabalhadas por um funcionário, informar o valor
# do seu salário líquido.

tra = int(input("Digite o numero de horas trabalhadas: "))

hora = 40.50

cont = tra * hora

if cont > 2500:
    imp = cont - ((cont * 11)/100) 
    print(f"O valor do salário liquido é: {imp}")

else:
    print(f"O valor do salário liquido é: {cont}")