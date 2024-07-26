def calcular_tempo(tempo_minutos):
    tempo_minimo_cobranca = 15
    valor_adicional_hora = 1.50
    valor_minimo = 9.00
    pis = 0.0033  # 0.33%
    cofins = 0.0020  # 0.20%
    icms = 0.17  # 17%
   
    # Se o tempo utilizado for menor que 15 minutos, não será cobrado
    if tempo_minutos < tempo_minimo_cobranca:
        return 0, 0
   
    horas_inteiras = tempo_minutos // 60
    minutos_adicionais = tempo_minutos % 60
   
    if minutos_adicionais > 0:
        horas_inteiras += 1
   
    if horas_inteiras > 1:
        valor_total = valor_minimo + (horas_inteiras - 1) * valor_adicional_hora
    else:
        valor_total = valor_minimo
   
    valor_pis = valor_total * pis
    valor_cofins = valor_total * cofins
    valor_icms = valor_total * icms
    total_impostos = valor_pis + valor_cofins + valor_icms
   
    valor_total_com_impostos = valor_total + total_impostos
    return valor_total_com_impostos, total_impostos
 
def imprimir_recibo(tempo_minutos, valor_total, total_impostos):
    print(f"Recibo Estacionamento")
    print(f"Valor Total a pagar: R$ {valor_total:.2f}")
    print(f"Impostos: R$ {total_impostos:.2f}")
    print(f"  - PIS (0.33%): R$ {valor_total * 0.0033:.2f}")
    print(f"  - COFINS (0.20%): R$ {valor_total * 0.0020:.2f}")
    print(f"  - ICMS (17%): R$ {valor_total * 0.17:.2f}")
 
tempo_utilizado = int(input("Digite o tempo utilizado no estacionamento em minutos: "))
valor_a_pagar, total_impostos = calcular_tempo(tempo_utilizado)
imprimir_recibo(tempo_utilizado, valor_a_pagar, total_impostos)