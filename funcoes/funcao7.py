def calculo_salario(horas_trabalhadas, salario_hora):
    carga_horaria_base = 40
    hora_extra = 1.5
   
    if horas_trabalhadas <= carga_horaria_base:
        salario_total = horas_trabalhadas * salario_hora
    else:
        quantidade_horas_extras = horas_trabalhadas - carga_horaria_base
        salario_base = carga_horaria_base * salario_hora
        salario_extra = quantidade_horas_extras * salario_hora * hora_extra
        salario_total = salario_base + salario_extra
    return salario_total
 
horas_trabalhadas = 45
salario_hora = 30
 
salario = calculo_salario(horas_trabalhadas, salario_hora)
print(f"O salário total a ser pago é: R$ {salario:.2f}")