def calculo_financiamento(valor_veiculo, entrada, taxa_juros, num_parcelas):
    valor_financiado = valor_veiculo - entrada
    taxa_juros_decimal = taxa_juros / 100
 
    parcela = valor_financiado * (taxa_juros_decimal * (1 + taxa_juros_decimal) ** num_parcelas) / ((1 + taxa_juros_decimal) ** num_parcelas - 1)
    valor_total_pago = parcela * num_parcelas
    juros_pagos = valor_total_pago - valor_financiado
    return valor_total_pago, juros_pagos, parcela
 
valor_veiculo = float(input("Digite o valor do veículo: "))
entrada = float(input("Digite o valor da entrada: "))
taxa_juros = float(input("Digite a taxa de juros mensal (em %): "))
num_parcelas = int(input("Digite o número de parcelas: "))
 
valor_total_pago, juros_pagos, parcela = calculo_financiamento(valor_veiculo, entrada, taxa_juros, num_parcelas)
 
print("\nResumo do Financiamento:")
print(f"Valor do veículo: R$ {valor_veiculo:.2f}")
print(f"Valor da entrada: R$ {entrada:.2f}")
print(f"Valor financiado: R$ {valor_veiculo - entrada:.2f}")
print(f"Taxa de juros mensal: {taxa_juros:.2f}%")
print(f"Número de parcelas: {num_parcelas}")
print(f"Valor de cada parcela: R$ {parcela:.2f}")
print(f"Valor total pago: R$ {valor_total_pago:.2f}")
print(f"Quantia dos juros pagos: R$ {juros_pagos:.2f}")