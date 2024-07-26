# Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar.
# As condições para aposentadoria são:
# • Ter pelo menos 65 anos,
# • Ou ter trabalhado pelo menos 30 anos,
# • Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

idade = int(input("Digite sua idade: "))
tempo_servico = int(input("Digite seu tempo de serviço em anos: "))

if idade >= 65 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25):
    print("Pode aposentar")

else:
    print("Não pode aposentar")