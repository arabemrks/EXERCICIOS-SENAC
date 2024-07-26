''''Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela que
considera o salário atual e o tempo de serviço de cada funcionário. Os funcionários com menor
salário terão um aumento proporcionalmente maior do que os funcionários com um salário
maior, e conforme o tempo de serviço na empresa, cada funcionário irá receber um bônus
adicional de salário. Crie um programa que leia:
• o valor do salário atual do funcionário;
• o tempo de serviço desse funcionário na empresa (número de anos de trabalho na
empresa).
Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor do
salário final reajustado, ou uma mensagem caso o funcionário não tenha direito a nenhum
aumento.
Salário Atual          Reajuste (%)            Tempo de Serviço          Bônus
Até 500,00                25%                  Abaixo de 1 ano         Sem bônus
Até 1000,00               20%                   De 1 a 3 anos            100,00
Até 1500,00               15%                   De 4 a 6 anos            200,00
Até 2000,00               10%                   De 7 a 10 anos           300,00
Acima de 2000,00     Sem reajuste              Mais de 10 anos           500,00
'''

salario = float(input("Digite o valor do salario atual: "))
tempo_servico = int(input("Digite o tempo de serviço: "))

if salario < 500 and tempo_servico < 1:
    reajuste = salario + (salario * 0.25)
    print(f"Valor do salário final com reajuste: {reajuste}")

elif salario < 1000 and 1 <= tempo_servico <= 3:
    reajuste = salario + (salario * 0.20) + 100
    print(f"Valor do salário final com reajuste: {reajuste}")

elif salario < 1500 and 4 <= tempo_servico <= 6:
    reajuste = salario + (salario * 0.15) + 200
    print(f"Valor do salário final com reajuste: {reajuste}")

elif salario < 2000 and 7 <= tempo_servico <= 10:
    reajuste = salario + (salario * 0.10) + 300
    print(f"Valor do salário final com reajuste: {reajuste}")

elif salario > 2000 and tempo_servico > 10:
    reajuste = salario + 500
    print(f"Valor do salário final com reajuste: {reajuste}")

else:
    print("Não tem direito a nenhum aumento")
