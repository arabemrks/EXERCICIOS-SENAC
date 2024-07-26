# A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso. Sendo que
# da quantia total:
# • O primeiro ganhador recebera 46%;
# • O segundo recebera 32%;
# • O terceiro recebera o restante;

valor = 780.000
x = valor * 0.46
y = valor * 0.32
z = valor - (x+y)

print(f"O primeiro ganhador receberá: {x}\n O segundo ganhador receberá: {y}\n O terceiro ganhador receberá: {z}")