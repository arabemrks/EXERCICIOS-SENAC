def calculo_tempo(tempo_minutos):
    tempo_minimo_cobranca = 15
    valor_adicional_hora = 1.50
    valor_minimo = 9.00
   
    if tempo_minutos < tempo_minimo_cobranca:
        return 0
   
    horas_inteiras = tempo_minutos // 60
    minutos_adicionais = tempo_minutos % 60
   
    if minutos_adicionais > 0:
        horas_inteiras += 1
   
    if horas_inteiras > 1:
        valor_total = valor_minimo + (horas_inteiras - 1) * valor_adicional_hora
    else:
        valor_total = valor_minimo
    return valor_total
 
tempo_utilizado = int(input("Digite o tempo utilizado no estacionamento em minutos: "))
valor_a_pagar = calculo_tempo(tempo_utilizado)
 
print(f"Valor a pagar é de: R$ {valor_a_pagar:.2f}")