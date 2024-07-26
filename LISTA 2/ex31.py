# Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um
# percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela abaixo:
# Consumo (Km/l) Mensagem
# menor que 8 Venda o carro!
# entre 8 e 14 Econômico!
# maior que 12 Super econômico!

distancia = float(input("Digite a distancia em km do percurso: "))
litros = float(input("Digite a quantidade de litros consumidos no percurso: "))

consumo = distancia/litros

if consumo <= 8:
    print("Venda o carro")

elif 8 <= consumo <= 14:
    print("Economico")

elif consumo > 12:
    print("Super economico")