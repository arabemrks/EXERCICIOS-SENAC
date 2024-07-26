def calculo_multa_peixe(peso_peixes):
    limite_peso = 50
    valor_multa_por_quilo = 4
   
    if peso_peixes > limite_peso:
        excesso = peso_peixes - limite_peso
        multa = excesso * valor_multa_por_quilo
    else:
        excesso = 0
        multa = 0
    return excesso, multa
 
peso_peixes = float(input("Digite o peso total de peixes em quilos: "))
excesso, multa = calculo_multa_peixe(peso_peixes)
 
print(f"Peso total de peixes: {peso_peixes:.2f} kg\nExcesso de peso: {excesso:.2f} kg\nValor da multa: R$ {multa:.2f}")