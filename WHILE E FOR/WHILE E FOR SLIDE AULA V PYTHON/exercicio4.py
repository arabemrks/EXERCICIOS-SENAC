avaliacoes = int(input("Digite o numero de avaliações do estudante: "))
i = 0
soma = 0
while i < avaliacoes:
    soma += float(input("Digite a nota: "))
    i += 1

media = soma/avaliacoes
print(media)
    